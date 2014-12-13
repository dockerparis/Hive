from django.shortcuts import render
from doct.app.models import Task
from doct.app.forms import TaskForm, ContributeForm

from django.http import HttpResponseRedirect

from doct.utils import docker

def home(request):
    return render(request, 'home.html')

def list_task(request):
    return render(request, 'list_task.html', {'tasks': Task.objects.all()})

def show_task(request, pk=None):
    try:
        task = Task.objects.get(id=pk)
    except:
        return HttpResponseRedirect("/")
    return render(request, 'show_task.html', {'task': task})


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
                                            gpu=form.cleaned_data['gpu'],
                                            disk_space=form.cleaned_data['disk_space'])

                return render(request, 'result_configuration.html', {'script': script})
        else:
            form = ContributeForm()
            return render(request, 'contribute_task.html', {'task': task, 'form': form})

    except:
        return HttpResponseRedirect("/list/")



