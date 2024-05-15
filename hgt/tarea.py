class Tarea:
    def __init__(self, tarea:str, estado:bool, id:str) -> None:
        self.tarea  = tarea
        self.id     = id
        self.estado = estado

    #Método CRUD
    def delete(self):
       self.estado = False

    
    def update(self, nueva_tarea:str):
        self.tarea = nueva_tarea

    
    def read(self):
        return self.tarea
        