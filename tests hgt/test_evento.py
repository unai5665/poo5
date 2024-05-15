import pytest
from test_evento import Evento


def test_evento():
    evento = Evento("Reunión de trabajo", True, "2", "2024-05-20")
   
    assert evento.read() == "Reunión de trabajo"
    evento.update("Entrevista de trabajo")
    assert evento.read() == "Entrevista de trabajo"
    evento.update_fecha("2024-05-25")
    assert evento.read_fecha() == "2024-05-25"