class Cine:
    def __init__(self, cine, direccion, funciones):
        self.cine = cine #es el nombre del cine
        self.direccion = direccion
        self.funciones = funciones
        self.open = True
        
    def info(self):
        print(f"Cine: {self.cine} \nDirección: {self.direccion}")
        S