from django.test import TestCase
from django.contrib.auth.models import User
from .models import Proyecto

class ProyectoTest(TestCase):
    def test_creacion_proyecto(self):
        user = User.objects.create(username="testuser")

        proyecto = Proyecto.objects.create(
            nombre="Test",
            descripcion="Desc",
            usuario=user
        )

        self.assertEqual(proyecto.nombre, "Test")