#determinante matriz cuadrada 5x5 con clases y TDA


class nodoMatriz:
    def __init__(self, valor):
        self.valor=valor
        self.siguiente=None
        self.anterior=None
        self.arriba=None
        self.abajo=None

class Matriz:
    def __init__(self, matriz):
        self.matriz=matriz
        self.crearMatriz()