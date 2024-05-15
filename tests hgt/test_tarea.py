import pytest
from .test_tarea import Tarea

def test_tarea():
    tarea = Tarea("Hacer la compra", True, "1")
    
    
    assert tarea.read() == "Hacer la compra"
    
    
    tarea.update("Pasear al perro")
    assert tarea.read() == "Pasear al perro"
    
   
    tarea.delete()
    assert tarea.estado == False