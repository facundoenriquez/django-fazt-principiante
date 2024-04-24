from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject
# Create your views here.


def hello(request, username):
    return HttpResponse('<h1>hello %s</h1>' % username)


def index(request):
    title = 'Welcome to Django !!!'
    return render(request, 'index.html', {
        'title': title
    })


def about(request):
    username = 'facudev'
    return render(request, 'about.html', {
        'username': username
    })


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })


def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(
            name=request.POST['name'])
        return redirect('projects')
