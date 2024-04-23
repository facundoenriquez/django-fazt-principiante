from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
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
    return render(request, 'projects.html',{
        'projects': projects
    })


def tasks(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'tasks.html')
