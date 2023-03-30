

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
        determinante=0
        if self.filas==2 and self.columnas==2:
            determinante=self.matriz[0][0]*self.matriz[1][1]-self.matriz[0][1]*self.matriz[1][0]
            print("El determinante de la matriz es: ", determinante)
        else:
            for i in range(self.filas):
                matrizAux=[]
                for j in range(self.filas):
                    if j!=i:
                        matrizAux.append(self.matriz[j])
                matrizAux.pop(0)
                for k in range(len(matrizAux)):
                    matrizAux[k].pop(0)
                determinante+=self.matriz[i][0]*self.determinanteAux(matrizAux)
            print("El determinante de la matriz es: ", determinante)

    def determinanteAux(self, matriz):
        determinante=0
        if len(matriz)==2:
            determinante=matriz[0][0]*matriz[1][1]-matriz[0][1]*matriz[1][0]
            return determinante
        else:
            for i in range(len(matriz)):
                matrizAux=[]
                for j in range(len(matriz)):
                    if j!=i:
                        matrizAux.append(matriz[j])
                matrizAux.pop(0)
                for k in range(len(matrizAux)):
                    matrizAux[k].pop(0)
                determinante+=matriz[i][0]*self.determinanteAux(matrizAux)
            return determinante
        
matriz=Matriz([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])

