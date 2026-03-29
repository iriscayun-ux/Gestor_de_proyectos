Descripción

Este es un proyecto realizado en Django para gestionar proyectos y tareas.

Permite:
-Crear y listar proyectos.
A-gregar tareas a cada proyecto.
-Controlar el estado de las tareas (Pendiente / Completado).
-Registro e inicio de sesión de usuarios.

Estructura del proyecto
gestor_tareas_proyecto/

 app # Aplicación principal
templates: # Archivos HTML
-403.html
-404.hmtl
-base.html
-home.html
-lista_proyectos.html
-crear_proyecto.html
-login.html
-register.html
- tareas.html

models.py    # Modelos de Proyecto y Tarea
views.py     # Vistas
forms.py     # Formularios personalizados
urls.py      # URLs de la app


 gestor_tareas_proyecto  # Configuración del proyecto
 -settings.py
 -urls.py
 -wsgi.py


 db.sqlite3    # Base de datos SQLite

Requisitos
Python 3.10+
Django 6.0+

Instalación de Django:
pip install django

Cómo ejecutar el proyecto
Clonar el repositorio:
git clone <tu-repo-url>
Entrar a la carpeta del proyecto:
cd gestor_tareas_proyecto

Aplicar migraciones:
python manage.py migrate
Crear superusuario (opcional):
python manage.py createsuperuser

Ejecutar el servidor:
python manage.py runserver

Abrir en el navegador:
http://127.0.0.1:8000/
Funcionalidades principales
Home: página principal iniciar sesion o registrare

Registro/Login: crear cuenta y acceder al sistema.

Proyectos:
Listar todos los proyectos del usuario.

Crear nuevo proyecto.
Botón para volver al listado desde “Crear Proyecto”.

Tareas:
Listar todas las tareas de un proyecto.
Visualizar estado y fechas.

Notas
Todos los proyectos y tareas están asociados al usuario que los creó.
Se utiliza base.html como plantilla principal para mantener consistencia en todas las páginas.
Bootstrap se usa para estilo básico y responsive.


Mi experiencia realizando el proyecto 

El objetivo principal fue aprender a implementar control de usuarios y permisos, manejo de formularios y vistas en Django, y personalizar templates de error.


Mostrar estado de las tareas en templates
Problema: inicialmente no se mostraba "Pendiente" o "Completado".
Solución: Se agregó un método estado en el modelo Tarea y se usó en el template.

Agregar campos de fecha sin romper migraciones
Problema: al agregar fecha_creacion con auto_now_add, Django pedía un valor por defecto para registros existentes.
Solución: se usó timezone.now como valor por defecto durante makemigrations.

Control de permisos 403
Problema: usuarios podían intentar acceder a proyectos ajenos cambiando el ID en la URL.
Solución: en lista_tareas, se verifica que proyecto.usuario == request.user; si no, se lanza PermissionDenied.

Advertencia en login personalizado
Problema: al ingresar credenciales incorrectas, no había feedback.
Solución: se sobrescribió form_invalid en CustomLoginView y se usó messages.error con Bootstrap.

Estilo y legibilidad de tablas
Problema: tabla de tareas no mostraba badges ni fechas bien formateadas.
Solución: se agregó |date:"d/m/Y" y clases de Bootstrap para mejorar visualización.



