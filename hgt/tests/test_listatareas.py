from listatareas import ListaTareas
import pytest

@pytest.fixture
def lista():
    return ListaTareas()

# Test de la clase ListaTareas
def test_listaTareas0(lista):
    assert len(lista) == 0

def test_listaTareas1(lista):
    lista.agregar('Programación')
    assert len(lista) == 1

def test_listaTarea2(lista):
    lista.agregar('Programación')
    lista.agregar('ETS')

    assert len(lista) == 2

    assert lista[0] == 'Programación'
    assert lista[1] == 'ETS'

def test_listaTareaDelete(lista):
    lista.agregar('Sistemas')
    assert lista[0] == 'Sistemas'

    del lista[0]
    assert len(lista) == 0

    assert 'Sistemas' not in lista

def test_listaRead(lista):
    lista.agregar('Programación')
    lista.agregar('ETS')

    assert lista.read() == 'Programación' + lista.LIMITCHAR + 'ETS'

def test_listaLoad(lista):
    lista.load('Programación' + lista.LIMITCHAR + 'ETS')
    assert len(lista) == 2

    assert lista[0] == 'Programación'
    assert lista[1] == 'ETS'