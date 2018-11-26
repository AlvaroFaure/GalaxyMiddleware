from django.shortcuts import render
from GalaxyStats.models import *

def registerStats(request):
    istekler = User.objects.all()
    return render(request, 'registerStats.html', locals())

def processesStats(request):
	istekler = User.objects.all()
	return render(request, 'processesStats.html', locals())

def workflowsStats(request):
	istekler = User.objects.all()
	return render(request, 'workflowsStats.html', locals())