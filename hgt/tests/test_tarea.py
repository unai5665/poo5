import pytest
from tarea import Tarea

@pytest.fixture
def tarea():
    return Tarea("Tarea1", True, 1)

def test_tarea_read(tarea):
     assert tarea.read() == "Tarea1, True, 1"

def test_tarea_update(tarea):
    tarea.update("Tarea2", False, 6)
    assert tarea.reas() == "Tarea1, False, 6"
    
def test_tarea_delete(tarae):    
    tarea.delete()
    assert tarea.read == "None, None, None"