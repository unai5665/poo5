from tarea import Tarea

class Evento(Tarea):
    def read(self) -> str:
        return super().read()

    def update_fecha(self, nueva_fecha: str):
        self.fecha = nueva_fecha

    def read_fecha(self):
        return self.fecha