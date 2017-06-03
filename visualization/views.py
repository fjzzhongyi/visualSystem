import json
import os
import subprocess

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from common_static.py.visual_cloud_option import visual_cloud

alg_script_root_dir = './visualization/alg_scripts'
alg_output_root_dir = './visualization/static/output'
abandoned_form_inputs = ['csrfmiddlewaretoken', 'alg_name', 'alg_visual_type']


def visual_index(request):
    return HttpResponseRedirect(reverse('visual_intro'))


def visual_intro(request):
    return render(request, 'visual_intro.html', visual_cloud)


def visual_alg(request, alg_visual_type, alg_name):
    visual_cloud['alg'] = visual_cloud['algs_info'][alg_visual_type][alg_name]
    return render(request, visual_cloud['algs_info'][alg_visual_type][alg_name]['html'], visual_cloud)


def submit_alg_data(request):
    platform_py_command = 'python2 '
    # Get alg data.
    alg_name = request.POST['alg_name']
    alg_visual_type = request.POST['alg_visual_type']
    alg_args_form_dict = visual_cloud['algs_info'][alg_visual_type][alg_name]['form']
    alg_args_list = sorted(alg_args_form_dict.keys())
    alg_args_list.remove('input_file')
    args_str = ''
    for key in alg_args_list:
        if key != 'input_file':
            args_str += ' --%s %s' % (key, request.POST[key])

    # Set alg output buf dir str named by args.
    alg_args_buf_dir = '_'.join(list(map(lambda sorted_key: request.POST[sorted_key], alg_args_list)))

    # Set relevant path.
    alg_input_file_path = './visualization/alg_scripts/MGraph/Graph.json'
    alg_output_dir = '%s/%s/%s' % (alg_output_root_dir, alg_name, alg_args_buf_dir)
    alg_script_path = alg_script_root_dir + '/MGraph/sdspark/SubgraphDetection.py'
    if os.name == 'nt':
        platform_py_command = 'py -2 '
    elif os.name == 'posix':
        platform_py_command = 'python2 '
    exec_alg_cmd = platform_py_command + alg_script_path + \
                   ' --inputfile ' + alg_args_form_dict['input_file']['options'][request.POST['input_file']] + \
                   ' --outputdir '+ alg_output_dir + args_str
    print(exec_alg_cmd)

    # Run the script.
    if not os.path.exists(alg_output_dir) or len(os.listdir(alg_output_dir)) == 0:
        try:
            os.makedirs(alg_output_dir)
        except FileExistsError as e:
            print(e)
        subprocess.run(exec_alg_cmd)

    # Get result.
    options = []
    timeline_data = []
    result_output_list = os.listdir(alg_output_dir)
    result_output_list.remove('cpu_memo_log')
    for i, filename in enumerate(sorted(result_output_list, key=lambda filename: int(filename.split('_')[0]))):
        with open('%s/%s' % (alg_output_dir, filename)) as output_json:
            def wrap_node(node):
                if node['selected']:
                    node['symbol'] = 'diamond'
                    node['symbolSize'] = 20
                return node

            json_obj = json.loads(output_json.read())
            json_obj['nodes'] = list(map(wrap_node, json_obj['nodes']))

            options.append({
                'series': {
                    'data': json_obj['nodes'],
                    'links': json_obj['edges']
                }
            })
        timeline_data.append(i)

    # Get cpu and mem info.
    cpu_data = []
    rss_data = []
    vms_data = []
    with open(alg_output_dir + '/cpu_memo_log') as cpu_memo_log:
        log_items_list = cpu_memo_log.readlines()
        for log_item_str in log_items_list:
            log_item = log_item_str.strip().split(' ')
            log_time = float(log_item[0]) * 1000
            cpu_data.append([log_time, log_item[1]])
            rss_data.append([log_time, log_item[2]])
            vms_data.append([log_time, log_item[3]])

    return JsonResponse({
        'chart_data': {
            'options': options,
            'timeline_data': timeline_data
        },
        'cpu_chart_data': cpu_data,
        'mem_chart_data': {
            'rss_data': rss_data,
            'vms_data': vms_data,
        }
    })