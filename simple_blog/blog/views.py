from django.shortcuts import render
from django.http import HttpResponse
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
    formulario = BlogForm(request)
    return render(request, 'nuevo_blog/crear.html'), {'formulario': formulario}

def editar(request):
    return render(request, 'nuevo_blog/editar.html')