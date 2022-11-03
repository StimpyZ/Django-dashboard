from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Elementos, Elementos1, Elementos2
from .forms import ElementForm, ElementForm1, ElementForm2
from django.contrib import messages
# Create your views here.

def index(request):
    elemento = Elementos.objects.all()
    elemento_count = elemento.count()
    elemento1 = Elementos1.objects.all()
    elemento1_count = elemento1.count()
    elemento2 = Elementos2.objects.all()
    elemento2_count = elemento2.count()

    if request.method == 'POST':
        form = ElementForm1(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = request.user
            obj.save()
            return redirect('dashboard-index')
    else:
        form = ElementForm1()
    context = {
        'form': form,
        'elemento': elemento,
        'elemento1': elemento1,
        'elemento2': elemento2,
        'elemento_count': elemento_count,
        'elemento1_count': elemento_count,
        'elemento2_count': elemento2_count,
    }
    return render(request, 'dashboard/index.html', context)

def nacidos(request):
    elemento = Elementos.objects.all()
    elemento_count = elemento.count()
    elemento1 = Elementos1.objects.filter()
    elemento1_count = elemento1.count()
    elemento2 = Elementos2.objects.all()
    elemento2_count = elemento2.count()
    elemento_quantity = Elementos.objects.filter()
    if request.method == 'POST':
        form = ElementForm(request.POST)
        if form.is_valid():
            form.save()
            elemento_name = form.cleaned_data.get('name')
            messages.success(request, f'{elemento_name} has been added')
            return redirect('dashboard-nacidos')
    else:
        form = ElementForm()
    context = {
        'elemento': elemento,
        'form': form,
        'elemento_count': elemento_count,
        'elemento1_count': elemento1_count,
        'elemento2_count': elemento2_count,
    }
    return render(request, 'dashboard/nacidos.html', context)


def pobrezacar(request):
    elemento = Elementos.objects.all()
    elemento_count = elemento.count()
    elemento1 = Elementos1.objects.filter()
    elemento1_count = elemento1.count()
    elemento2 = Elementos2.objects.all()
    elemento2_count = elemento2.count()
    elemento1_quantity = Elementos1.objects.filter()
    if request.method == 'POST':
        form = ElementForm1(request.POST)
        if form.is_valid():
            form.save()
            elemento_name1 = form.cleaned_data.get('name')
            messages.success(request, f'{elemento_name1} has been added')
            return redirect('dashboard-pobrezacar')
    else:
        form = ElementForm1()
    context = {
        'elemento1': elemento1,
        'form': form,
        'elemento_count': elemento_count,
        'elemento1_count': elemento1_count,
        'elemento2_count': elemento2_count,
    }
    return render(request, 'dashboard/pobrezacar.html', context)


def matriculacar(request):
    elemento = Elementos.objects.all()
    elemento_count = elemento.count()
    elemento1 = Elementos1.objects.all()
    elemento1_count = elemento1.count()
    elemento2 = Elementos2.objects.all()
    elemento2_count = elemento2.count()
    elemento2_quantity = Elementos2.objects.filter()
    if request.method == 'POST':
        form = ElementForm2(request.POST)
        if form.is_valid():
            form.save()
            elemento_name2 = form.cleaned_data.get('name')
            messages.success(request, f'{elemento_name2} has been added')
            return redirect('dashboard-matriculacar')
    else:
        form = ElementForm2()
    context = {
        'elemento2': elemento2,
        'form': form,
        'elemento_count': elemento_count,
        'elemento1_count': elemento1_count,
        'elemento2_count': elemento2_count,
    }
    return render(request, 'dashboard/matriculacar.html', context)


def nacidos_delete(request, pk):
    item = Elementos.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-nacidos')
    context = {
        'item': item
    }
    return render(request, 'dashboard/nacidosdelete.html', context)


def matriculacar_delete(request, pk):
    item = Elementos2.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-matriculacar')
    context = {
        'item': item
    }
    return render(request, 'dashboard/matriculacardelete.html', context)

def pobrezacar_delete(request, pk):
    item = Elementos1.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-pobrezacar')
    context = {
        'item': item
    }
    return render(request, 'dashboard/pobrezacardelete.html', context)