# Archivo de pruebas: test_models.py

import pytest
from django.db import IntegrityError
from api.models import registros

@pytest.mark.django_db
def test_create_and_query_registro():
    # Crear un registro
    registro = registros.objects.create(name="John Doe", email="john@example.com", password="secure_password")

    # Consultar el registro recién creado
    queried_registro = registros.objects.get(name="John Doe")

    assert queried_registro is not None
    assert queried_registro.name == "John Doe"
    assert queried_registro.email == "john@example.com"
    assert queried_registro.password == "secure_password"

@pytest.mark.django_db
def test_unique_email_constraint():
    # Asegurarse de que el campo de correo electrónico sea único
    registros.objects.create(name="User 1", email="user@example.com", password="password")
    with pytest.raises(IntegrityError):
        registros.objects.create(name="User 2", email="user@example.com", password="password")
