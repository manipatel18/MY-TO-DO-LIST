from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
            return redirect('home')

    tasks = Task.objects.all()
    return render(request, 'home.html',{'tasks':tasks})


def delete_task(request, pk):
    task = get_object_or_404(Task,id= pk)
    task.delete()
    return redirect('home')

def edit_task(request, id):
    task = Task.objects.get(id=id)

    if request.method == "POST":
        title = request.POST.get('title')
        
        if title:
            task.title = title
            task.save()
            return redirect('/')
    return render(request, 'edit.html',{'task': task})          


def update_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.title = request.POST.get('title')
        task.save()
        return redirect('home')


def toggle_complete(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.completed = not task.completed
    task.save()
    return redirect('home')