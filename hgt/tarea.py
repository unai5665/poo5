class Tarea:
    def __init__(self, tarea:str, estado:bool, id:int) -> None:
        self.tarea  = tarea
        self.id     = id
        self.estado = estado

    #Método CRUD
    def read(self)->str:
        return f"{self.tarea}, {self.estado}, {self.id}"
    

    def update(self, nueva_tarea:str, nuevo_estado:bool, nuevo_id:int)->None:
        self.tarea = nueva_tarea
        self.id = nuevo_id
        self.estado = nuevo_estado 

    def delete(self):
       self.estado = None
       self.id = None
       self.estado = None

    
    

    
    
        