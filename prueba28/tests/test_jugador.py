import pytest

from prueba28.jugador.jugador import Jugador


@pytest.fixture
def jugador():
    return Jugador('William', 'Criket')

def test_read(jugador):
    assert jugador.read() == "William,Criket"