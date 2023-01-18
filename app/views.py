from django.shortcuts import render, redirect
from app.forms import ProdutoForm
from app.models import Produto

def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Produto.objects.filter(modelo__icontains=search)
    else:
        data['db'] = Produto.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = ProdutoForm()
    return render(request, 'form.html', data)

def create(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data= {}
    data['db'] = Produto.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data= {}
    data['db'] = Produto.objects.get(pk=pk)
    data['form'] = ProdutoForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    form = ProdutoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Produto.objects.get(pk=pk)
    db.delete()
    return redirect('home')