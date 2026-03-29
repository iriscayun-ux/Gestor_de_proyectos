from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #HOME
    path('', views.home, name='home'),

    #AUTENTICACIÓN
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

    #PROYECTOS
    path('proyectos/', views.lista_proyectos, name='lista_proyectos'),
    path('crear/', views.crear_proyecto, name='crear_proyecto'),

    #TAREAS
    path('tareas/<int:proyecto_id>/', views.lista_tareas, name='lista_tareas'),
]