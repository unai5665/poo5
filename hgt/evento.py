from tarea import Tarea

class Evento(Tarea):
    def __init__(self, tarea: str, estado: bool, id: str) -> None:
        super().__init__(tarea, estado, id)