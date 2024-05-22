from tarea import Tarea
class ListaTareas:
    LIMITCHAR = "|&&|"

    def __init__(self, lista:list) -> None:
        self.lista = []

    def agregar(self, tarea:Tarea ):
        self.lista.append(tarea)
    
    def read(self):
        result = ""
        for tarea in self.lista:
            result += tarea
            if tarea != self.lista[-1]:
                result += self.LIMITCHAR
        
        return result
    

    def load(self, data:str):
        tarea = data.split(self.LIMITCHAR)
        for tarea in self.lista:
            self.lista.append(tarea)


    def update(self, tarea:Tarea, newtarea:str, estado:bool, id:int):
        for a in self.lista:
            if a == tarea:
                a.update(newtarea)
                a.update(estado)
                a.update(id)
                break

    def delete(self, tarea:Tarea):
        for a in self.lista:
            if a == tarea:
                a.delete()
                break

    def __str__(self) -> str:
        return self.read()
    
    def __len__(self):
        return self.lista.__len__()
    
    def __getitem__(self, index):
        return self.lista[index]
    
    def __setitem__(self, index, value):
        self.lista[index] = value

    def __iter__(self):
        return self.lista.__iter__()
    
    def __next__(self):
        return self.lista.__next__()
    
    def __contains__(self, item):
        return item in self.lista
    
    def __eq__(self, other):
        return self.lista == other.lista
    
    def __ne__(self, other):
        return self.lista != other.lista