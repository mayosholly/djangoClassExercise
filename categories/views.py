from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import CategoryForm

def index(request):
    categories = Category.objects.all()
    return render(request, 'categories/index.html', {'categories': categories})

def create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories:index')
    else:
        form = CategoryForm()
    return render(request, 'categories/form.html', {'form': form})

def edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories:index')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/form.html', {'form': form})

def show(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'categories/show.html', {'category': category})

def delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories:index')
    return render(request, 'categories/confirm_delete.html', {'category': category})
