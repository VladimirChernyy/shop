from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def catalog(request):
    tasks = Task.objects.all()
    return render(request, 'main/catalog.html', {'title': 'Каталог', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog')
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/create.html', context)


def manual_tile_сutter(request):
    return render(request, 'main/manual_tile_сutter.html')


def electric_tile_cutter(request):
    return render(request, 'main/electric_tile_cutter.html')

def XL_size(request):
    return render(request, 'main/XL_size.html')