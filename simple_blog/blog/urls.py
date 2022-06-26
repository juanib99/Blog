from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/crear/', views.crear_blogs, name='crear_blogs'),
    path('blogs/editar/', views.editar, name='editar'),

]