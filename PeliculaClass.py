class Pelicula:
    def __init__(self,nombre, descripcion, genero, duracion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.genero = genero
        self.duracion = duracion
    def info(self):
        
        print(f"Pelicula: {self.nombre} \nDecripción: {self.descripcion} \nGénero{self.genero} \n Duración:{self.duracion}")
