from django.shortcuts import render
from doct.app.models import Task, StatTask
from doct.app.forms import TaskForm, ContributeForm

from django.http import HttpResponseRedirect, HttpResponse

from doct.utils import docker

# to get and parse stat
import requests
from xml.dom import minidom
from datetime import datetime, timedelta

# search task
import json

# trending project
from django.db.models import Count

def home(request):
    trending_projects = StatTask.objects.annotate(Count('number_users')).order_by('number_users')[:3]
    return render(request, 'home.html', {'trending_projects': trending_projects})

def list_task(request, pk=None):
    if pk == None or pk <= 0:
        pk = 1
    else:
        pk = int(pk)
    tasks = Task.objects.all()
    return render(request, 'list_task.html', {'tasks': tasks[(pk - 1) * 10: pk * 10], 'current_page': pk, 'number_pages': range(1, tasks.count() / 10  + 2)})

def show_task(request, pk=None):
    try:
        task = Task.objects.get(id=pk)
    except:
        return HttpResponseRedirect("/")
    stat = getStatForTask(task)
    return render(request, 'show_task.html', {'task': task, 'stat': stat})


def update_task(request, pk=None):
    try:
        task = Task.objects.get(id=pk)
    except:
        return HttpResponseRedirect("/")
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            task.save()
            return HttpResponseRedirect("/list/")
    elif pk is not None:
        form = TaskForm(instance=task)
        return render(request, 'create_task.html', {'form': form})

def new_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.save()
            return HttpResponseRedirect("/list/")
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

def contribute_task(request, pk=None):
    try:
        task = Task.objects.get(id=pk)

        if request.method == "POST":
            form = ContributeForm(request.POST)
            if form.is_valid():
                script = docker.generate_configuration(
                                            link=task.link,
                                            ram=form.cleaned_data['ram'],
                                            cpu=form.cleaned_data['cpu'],
                                            # gpu=form.cleaned_data['gpu'],
                                            disk_space=form.cleaned_data['disk_space'])
                return render(request, 'result_configuration.html', {'script': script})
            else:
                return render(request, 'contribute_task.html', {'task': task, 'form': form})
        else:
            form = ContributeForm()
            return render(request, 'contribute_task.html', {'task': task, 'form': form})

    except Exception, e:
        print e
        return HttpResponseRedirect("/list/")


def getStatForTask(task):
    try:
        stat = StatTask.objects.get(task=task)
        if stat.update_time_db.replace(tzinfo=None) > datetime.now() - timedelta(hours=24):
            return stat
    except Exception, e:
        print e
        stat = None

    if stat is None:
        stat = StatTask()
        stat.task = task
    try:
        link_xml = task.link
        if task.link[:-1] is not '/':
            link_xml += '/'
        link_xml += 'stats/tables.xml'
        tables_xml = requests.get(link_xml)
    except:
        return None

    if tables_xml.status_code == 200:
        try:
            xml_doc = minidom.parseString(tables_xml.content)
            timestamp = xml_doc.getElementsByTagName('update_time')[0].childNodes[0].data
            stat.update_time = datetime.fromtimestamp(float(timestamp))
            stat.number_users = xml_doc.getElementsByTagName('nusers_total')[0].childNodes[0].data
            stat.number_teams = xml_doc.getElementsByTagName('nteams_total')[0].childNodes[0].data
            stat.number_hosts = xml_doc.getElementsByTagName('nhosts_total')[0].childNodes[0].data
            stat.total_credit = xml_doc.getElementsByTagName('total_credit')[0].childNodes[0].data
        except:
            print "Error parsing"
            return None
    else:
        print "Can't fetch stats"
        return None
    stat.save()
    return stat


def search_task(request):
    try:
        if request.is_ajax():
            q = request.GET.get('term', '')
            tasks = Task.objects.filter(title__contains = q )[:20]
            results = []
            for task in tasks:
                task_json = {}
                task_json['id'] = task.id
                task_json['label'] = task.title
                task_json['value'] = task.link
                results.append(task_json)
            data = json.dumps(results)
        else:
            data = 'fail'
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)
    except Exception, e:
        print e
