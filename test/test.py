from src.main import *
from unittest.mock import patch

def test_root():
    assert root() == {"Hello": "World"}

def test_funcaoteste():
    with patch("dandom.randint", return_value=12345):
        result = funcaoteste()
    assert result == {"teste": True, "num_aleatorio": 12345}


def test_create_estudante(estudante: Estudante):
    estudante_teste = Estudante(name="Adriano", curso="Matemática", ativo=False)
    assert estudante_teste == create_estudante(estudante_teste)


def test_update_estudante_negativo():
    assert not update_estudante(-5)

def test_update_estudante_positivo():
    assert not update_estudante(10)

def test_delete_estudante_negativo():
    assert not delete_estudante(-5)

def test_delete_estudante_positivo():
    assert not delete_estudante(10)