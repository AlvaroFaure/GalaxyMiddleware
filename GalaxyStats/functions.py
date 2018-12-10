from django.http import JsonResponse
from django.http import HttpResponse
import json, csv, os
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from GalaxyStats.models import *
import subprocess, re
from django.core import serializers

from django.apps import apps 

@csrf_exempt
def register(request):

	if request.method == 'GET':

		data = serializers.serialize("json", User.objects.all())

		return HttpResponse(data, content_type="application/json")

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
def processesView(request):

	if request.method == 'POST':

		return HttpResponse('No definido', content_type="text/plain")

	elif request.method == 'GET':

		subprocess.call(['./GalaxyStats/bash/processes.sh','./GalaxyStats/bash/procesos.txt'])

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
def processes(request):

	if request.method == 'POST':

		return HttpResponse('No definido', content_type="text/plain")

	elif request.method == 'GET':

		subprocess.call(['./GalaxyStats/bash/processes.sh','./GalaxyStats/bash/procesos.txt'])

		file  = open("./GalaxyStats/bash/procesos.txt", "r")

		file.readline()
		file.readline()

		lines = file.readlines()[:-2]

		final = ""

		for line in lines:
			line = re.sub(" \| ",",",line)
			line = re.sub("[ ][ ]+","",line)
			line = re.sub("^[ ]","",line)
			line = re.sub(",\n",",NULL\n",line)
			final = final + line   

		csvfile = open('./GalaxyStats/bash/file.csv', 'w')
		csvfile.write(final)
		csvfile.close()

		csvfile = open('./GalaxyStats/bash/file.csv', 'r')
		jsonfile = open('./GalaxyStats/bash/file.json', 'w')
		fieldnames = ("id","create_time","tool_id","exit_code")

		reader = csv.DictReader(csvfile, fieldnames)

		for row in reader:
			json.dump(row, jsonfile)
			jsonfile.write('\n')

		jsonfile.close()
		csvfile.close()

		jsonfile = open('./GalaxyStats/bash/file.json', 'r')
		final = jsonfile.read()
		jsonfile.close()

		if os.path.exists('./GalaxyStats/bash/file.json'):
			os.remove('./GalaxyStats/bash/file.json')

		if os.path.exists('./GalaxyStats/bash/file.csv'):
			os.remove('./GalaxyStats/bash/file.csv')

		return HttpResponse(final, content_type="application/json")

		

@csrf_exempt
def workflowsView(request):

	if request.method == 'POST':

		return HttpResponse('No definido', content_type="text/plain")

	elif request.method == 'GET':

		subprocess.call(['./GalaxyStats/bash/workflows.sh','./GalaxyStats/bash/workflows.txt'])

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

@csrf_exempt
def workflows(request):

	if request.method == 'POST':

		return HttpResponse('No definido', content_type="text/plain")

	elif request.method == 'GET':

		subprocess.call(['./GalaxyStats/bash/workflows.sh','./GalaxyStats/bash/workflows.txt'])

		file  = open("./GalaxyStats/bash/workflows.txt", "r")

		file.readline()
		file.readline()

		lines = file.readlines()[:-2]

		final = ""

		for line in lines:
			line = re.sub(" \| ",",",line)
			line = re.sub("[ ][ ]+","",line)
			line = re.sub("^[ ]","",line)
			final = final + line

		csvfile = open('./GalaxyStats/bash/file.csv', 'w')
		csvfile.write(final)
		csvfile.close()

		csvfile = open('./GalaxyStats/bash/file.csv', 'r')
		jsonfile = open('./GalaxyStats/bash/file.json', 'w')
		fieldnames = ("id","create_time","name","workflow_step_id")

		reader = csv.DictReader(csvfile, fieldnames)

		for row in reader:
			json.dump(row, jsonfile)
			jsonfile.write('\n')

		jsonfile.close()
		csvfile.close()

		jsonfile = open('./GalaxyStats/bash/file.json', 'r')
		final = jsonfile.read()
		jsonfile.close()

		if os.path.exists('./GalaxyStats/bash/file.json'):
			os.remove('./GalaxyStats/bash/file.json')

		if os.path.exists('./GalaxyStats/bash/file.csv'):
			os.remove('./GalaxyStats/bash/file.csv')

		return HttpResponse(final, content_type="application/json")
