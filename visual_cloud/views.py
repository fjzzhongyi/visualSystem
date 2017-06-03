from django.shortcuts import render
from common_static.py.visual_cloud_option import visual_cloud


def home(request):
    return render(request, 'home.html', visual_cloud)


def management(request):
    return render(request, 'management.html', visual_cloud)


def about(request):
    return render(request, 'about.html', visual_cloud)