from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('home')

    tasks = Task.objects.all()
    return render(request, 'home.html',{'tasks':tasks})


def delete_task(request, pk):
    task = get_object_or_404(Task,id= pk)
    task.delete()
    return redirect('home')

def toggle_complete(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.completed = not task.completed
    task.save()
    return redirect('home')