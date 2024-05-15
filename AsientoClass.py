class Asiento:
    def __init__(self, fila, numero):
        self.fila = fila
        self.numero = numero
        self.ocupado = False
        
    def marcar0cupado(self):
        self.ocupado = True