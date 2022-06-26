from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Blog
from .forms import BlogForm
# Create your views here.

def inicio(request):
    return render(request, 'blog/inicio.html')

def nosotros(request):
    return render(request, 'blog/nosotros.html')

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'nuevo_blog/bases.html', {'blogs': blogs})

def crear_blogs(request):
    formulario = BlogForm(request or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('blogs')
    return render(request, 'nuevo_blog/crear.html'), {'formulario': formulario}

def editar(request, id):
    blog = Blog.objects.get(id=id)
    formulario = BlogForm(request.POST or None, request.FILES or None, instance=blog)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('blogs')
    return render(request, 'nuevo_blog/editar.html', {'formulario':formulario})

def eliminar(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('blogs')