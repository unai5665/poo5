from tarea import Tarea

class Evento(Tarea):
    def __init__(self, tarea: str, estado: bool, id: str, fecha: str) -> None:
        self.tarea = tarea
        self.id = id
        self.estado = estado
        self.fecha = fecha

    def update_fecha(self, nueva_fecha: str):
        self.fecha = nueva_fecha

    def read_fecha(self):
        return self.fecha