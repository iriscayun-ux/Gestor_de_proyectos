from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto, Tarea
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import ProyectoForm, CustomUserCreationForm
from django.contrib.auth import login
from django.core.exceptions import PermissionDenied
from django.contrib import messages

#LISTA DE PROYECTOS
@login_required
def lista_proyectos(request):
    proyectos = Proyecto.objects.filter(usuario=request.user)
    return render(request, 'lista_proyectos.html', {'proyectos': proyectos})

# LOGIN
class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_invalid(self, form):
        # Si login falla, mostrar mensaje de advertencia
        messages.error(self.request, "Usuario o contraseña incorrectos")
        return super().form_invalid(form)

#CREAR PROYECTO 
@login_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.usuario = request.user
            proyecto.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()

    return render(request, 'crear_proyecto.html', {'form': form})

#REGISTRO DE USUARIOS
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_proyectos')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

#LISTA DE TAREAS DE UN PROYECTO
@login_required
def lista_tareas(request, proyecto_id):
    # Obtener el proyecto y validar propiedad
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    if proyecto.usuario != request.user:
        # Usuario intenta acceder a un proyecto que no le pertenece
        raise PermissionDenied

    # Solo tareas del proyecto que pertenece al usuario
    tareas = Tarea.objects.filter(proyecto=proyecto)
    return render(request, 'tareas.html', {'tareas': tareas})

#HOME
def home(request):
    return render(request, 'home.html')