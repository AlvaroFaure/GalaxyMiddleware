from django.http import JsonResponse
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from GalaxyStats.models import *
import subprocess, re

from django.apps import apps 


@csrf_exempt
def register(request):

    if request.method == 'GET':

        #cadena = ""

        #for i in range(0,3):
        #   pais = User.objects.order_by().values_list('country').distinct()[i][0]
        #   cadena = cadena + "%s - %s" % (pais, User.objects.filter(country=pais).count()) + "\n"

        #return HttpResponse(User.objects.order_by().values_list('country').distinct(), content_type="text/plain")

        return HttpResponse('No definido', content_type="text/plain")

    elif request.method == 'POST':
        readable_json = json.loads(request.body.decode('utf-8'))

        email = readable_json["email"]
        public_name = readable_json["public_name"]
        country = readable_json["country"]
        institution = readable_json["institution"]

        app_models = apps.get_app_config('GalaxyStats').get_models()

        try:
            user = User.objects.get(pk=email)
        except User.DoesNotExist:
            user = None
        
        if user is None:
            user = User.objects.create(email=email, public_name=public_name, country=country, institution=institution)
            user.save()
            return HttpResponse("Usuario creado", content_type="text/plain")
        else:
            return HttpResponse("El usuario ya existe", content_type="text/plain")


@csrf_exempt
def processesStats(request):

    if request.method == 'POST':

        return HttpResponse('No definido', content_type="text/plain")

    elif request.method == 'GET':

        #subprocess.call(['./GalaxyStats/bash/processes.sh','./GalaxyStats/bash/procesos.txt'])

        file  = open("./GalaxyStats/bash/procesos.txt", "r")

        cabecera = file.readline()
        cabecera = re.sub(" \| ",",",cabecera)
        cabecera = line = re.sub("[ ]","",cabecera)

        file.readline()

        lines = file.readlines()[:-2]

        final = cabecera

        for line in lines:
        	line = re.sub(" \| ",",",line)
        	line = re.sub("[ ][ ]+","",line)
        	line = re.sub("^[ ]","",line)
        	line = re.sub(",\n",",NULL\n",line)
        	final = final + line       

        return HttpResponse(final, content_type="text/plain")

        

@csrf_exempt
def workflowsStats(request):

    if request.method == 'POST':

        return HttpResponse('No definido', content_type="text/plain")

    elif request.method == 'GET':

        #subprocess.call(['./GalaxyStats/bash/workflows.sh','./GalaxyStats/bash/workflows.txt'])

        file  = open("./GalaxyStats/bash/workflows.txt", "r")

        cabecera = file.readline()
        cabecera = re.sub(" \| ",",",cabecera)
        cabecera = line = re.sub("[ ]","",cabecera)

        file.readline()

        lines = file.readlines()[:-2]

        final = cabecera

        for line in lines:
        	line = re.sub(" \| ",",",line)
        	line = re.sub("[ ][ ]+","",line)
        	line = re.sub("^[ ]","",line)
        	final = final + line       

        return HttpResponse(final, content_type="text/plain")
