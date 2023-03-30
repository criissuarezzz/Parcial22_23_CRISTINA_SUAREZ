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
        self.filas=len(matriz)
        self.columnas=len(matriz[0])
        self.cabeza=None
        self.crearMatriz()
        self.determinante()

    def crearMatriz(self):
        self.cabeza=nodoMatriz(0)
        aux=self.cabeza
        for i in range(self.filas):
            for j in range(self.columnas):
                aux.siguiente=nodoMatriz(self.matriz[i][j])
                aux.siguiente.anterior=aux
                aux=aux.siguiente
            aux=self.cabeza
            for k in range(i+1):
                aux.abajo=nodoMatriz(0)
                aux.abajo.arriba=aux
                aux=aux.abajo
            aux=self.cabeza

    def determinante(self):
        