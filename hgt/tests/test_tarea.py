import pytest
from .test_tarea import Tarea

def test_tarea():
    tarea = Tarea("Hacer la tarea", True, "1")
    
    
    assert tarea.read() == "Hacer la tarea"
    
    
    tarea.update("Tarea hecha")
    assert tarea.read() == "Tarea hecha"
    
   
    tarea.delete()
    assert tarea.estado == False