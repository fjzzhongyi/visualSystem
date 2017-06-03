function createDemoChart(chart, demoType) {
    switch (demoType) {
        // case 'graph': createDemoGraphChart(chart);
        case 'dynamic':
            createDemoGraphChart(chart);
            break;
        case 'static':
            createDemoGraphChart(chart);
            break;
    }
}

function createDemoGraphChart(chart) {

    function createNodes(count) {
        var nodes = [];
        for (var i = 0; i < count; i++) {
            nodes.push({
                id: i
            });
        }
        return nodes;
    }

    function createEdges(count) {
        var edges = [];
        if (count === 2) {
            return [[0, 1]];
        }
        for (var i = 0; i < count; i++) {
            edges.push([i, (i + 1) % count]);
        }
        return edges;
    }

    var datas = [];
    for (var i = 0; i < 16; i++) {
        datas.push({
            nodes: createNodes(i + 2),
            edges: createEdges(i + 2)
        });
    }

    option = {
        title: {
            text: 'Graph Demo',
            right: 0,
            top: 0,
        },
        series: datas.map(function (item, idx) {
            return {
                type: 'graph',
                layout: 'force',
                animation: false,
                data: item.nodes,
                left: (idx % 4) * 25 + '%',
                top: Math.floor(idx / 4) * 25 + '%',
                width: '25%',
                height: '25%',
                force: {
                    // initLayout: 'circular'
                    // gravity: 0
                    repulsion: 60,
                    edgeLength: 2
                },
                edges: item.edges.map(function (e) {
                    return {
                        source: e[0],
                        target: e[1]
                    };
                }),
                draggable: true,
            };
        })
    };

    chart.setOption(option);
    window.onresize = chart.resize;
}

function createChart(chart, demoType, data) {
    switch (demoType) {
        // case 'graph':
        //     createGraph(chart, data);
        case 'dynamic':
            createGraph(chart, data);
            break;
        case 'static':
            createGraph(chart, data);
            break;
    }
}

function createGraph(chart, data) {
    var option = {
        baseOption: {
            legend: {
                show: true,
                orient: 'vertical',
                left: 'left',
                data: [{
                    name: 'normal',
                    icon: 'circle',
                    textStyle: {
                        color: 'black'
                    }
                }, {
                    name: 'abnormal',
                    icon: 'diamond',
                    textStyle: {
                        color: 'black'
                    }
                }]
            },
            toolbox: {
                show: true,
                feature: {
                    dataView: {readOnly: false},
                    restore: {},
                    saveAsImage: {}
                }
            },
            tooltip: {
                trigger: 'item'
            },
            timeline: {
                playInterval: 1000,
                axisType: 'value',
                data: []
            },
            visualMap: {
                min: 0,
                max: 1,
                show: false,
                inRange: {
                    colorLightness: [0.3, 0.8]
                }
            },
            series : [
                {
                    name: 'normal',
                    type: 'graph',
                    layout: 'force',
                    roam: true,
                    draggable: true,
                    label: {
                        normal: {
                            position: 'right'
                        }
                    },
                    force: {
                        repulsion: 100
                    }
                }
                ,{
                    name: 'abnormal',
                    type: 'graph',
                }
            ]
        },
        options: []
    };
    option.baseOption.timeline.data = data.timeline_data;
    option.options = data.options;
    chart.setOption(option);
}

function createCPULine(chart, data) {
    var option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                animation: false
            }
        },
        xAxis: {
            type: 'time',
            axisLabel: {
                formatter: function (value, index) {
                    var date = new Date(value);
                    var texts = [date.getHours(), date.getMinutes(), date.getSeconds()];
                    return texts.join(':');
                }
            }
        },
        yAxis: {
            type: 'value',
        },
        series: [
            {
                name: 'CPU Usage',
                type: 'line',
                showSymbol: false,
                data: data
            }
        ]
    };
    chart.setOption(option);
}

function createMemLine(chart, data) {
    var option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                animation: false
            }
        },
        xAxis: {
            type: 'time',
            axisLabel: {
                formatter: function (value, index) {
                    var date = new Date(value);
                    var texts = [date.getHours(), date.getMinutes(), date.getSeconds()];
                    return texts.join(':');
                }
            }
        },
        yAxis: {
            type: 'value',
        },
        series: [
            {
                name: 'RSS Usage',
                type: 'line',
                showSymbol: false,
                data: data.rss_data
            },
                        {
                name: 'VMS Usage',
                type: 'line',
                showSymbol: false,
                data: data.vms_data
            }
        ]
    };
    chart.setOption(option);
}