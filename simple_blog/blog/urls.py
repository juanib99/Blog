from django.urls import path
from . import views

# from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/crear/', views.crear_blogs, name='crear_blogs'),
    path('blogs/editar/', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('blogs/editar/<int:id>', views.editar, name='editar'),

]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)