from django.shortcuts import render
from GalaxyStats.models import *

def registerView(request):
    istekler = User.objects.all()
    return render(request, 'registerView.html', locals())