# test.py
import pytest
from calc import suma

def test_suma_enteros():
    assert suma(2, 3) == 5

def test_suma_decimales():
    assert suma(2.5, 3.5) == 6.0

def test_suma_mixta():
    assert suma(2, 3.5) == 5.5

def test_suma_error():
    assert suma(2, "texto") == "error"
            