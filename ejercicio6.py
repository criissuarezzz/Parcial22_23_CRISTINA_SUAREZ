def iterativo():
    print('\033[35m'+ "DE MANERA ITERATIVA " + '\033[0m')
    matriz=[]
    for i in range(5):
        matriz.append([])
        for j in range(5):
            matriz[i].append(int(input("ingrese el numero de la posicion ["+str(i)+"]["+str(j)+"]: ")))
    print("la matriz es: ")
    for i in range(5):
        for j in range(5):
            print(matriz[i][j], end=" ")
        print()

    print('\033[36m'+"¿desea cambiar algún numero de la matriz? (si/no)"+'\033[0m')
    respuesta = input("->")
    if respuesta == "si":
        print("ingrese la posicion del numero que desea cambiar")
        print("fila: ")
        fila = int(input("->"))
        print("columna: ")
        columna = int(input("->"))
        print("ingrese el nuevo numero: ")
        numero = int(input("->"))
        matriz[fila][columna] = numero
        print("la matriz es: ")
        for i in range(5):
            for j in range(5):
                print(matriz[i][j], end=" ")
            print()
    else:
        print("la matriz se queda igual")
    determinante = matriz[0][0]*matriz[1][1]*matriz[2][2]*matriz[3][3]*matriz[4][4] + matriz[0][1]*matriz[1][2]*matriz[2][3]*matriz[3][4]*matriz[4][0] + matriz[0][2]*matriz[1][3]*matriz[2][4]*matriz[3][0]*matriz[4][1] + matriz[0][3]*matriz[1][4]*matriz[2][0]*matriz[3][1]*matriz[4][2] + matriz[0][4]*matriz[1][0]*matriz[2][1]*matriz[3][2]*matriz[4][3] - matriz[0][4]*matriz[1][3]*matriz[2][2]*matriz[3][1]*matriz[4][0] - matriz[0][3]*matriz[1][2]*matriz[2][1]*matriz[3][0]*matriz[4][4] - matriz[0][2]*matriz[1][1]*matriz[2][0]*matriz[3][4]*matriz[4][3] - matriz[0][1]*matriz[1][0]*matriz[2][4]*matriz[3][3]*matriz[4][2] - matriz[0][0]*matriz[1][4]*matriz[2][3]*matriz[3][2]*matriz[4][1] #utilizamos la fórmula del determinante de una matriz cuadrada de 5x5
    print("el determinante de la matriz es: ", determinante)
    print('\033[35m'+ "===================" + '\033[0m')


def recursivo():
    print('\033[35m'+ "DE MANERA RECURSIVA " + '\033[0m')
    matriz=[]
    for i in range(5):
        matriz.append([])
        for j in range(5):
            matriz[i].append(int(input("ingrese el numero de la posicion ["+str(i)+"]["+str(j)+"]: ")))
    print("la matriz es: ")
    for i in range(5):
        for j in range(5):
            print(matriz[i][j], end=" ")
        print()

    print('\033[36m'+"¿desea cambiar algún numero de la matriz? (si/no)"+'\033[0m')
    respuesta = input("->")
    if respuesta == "si":
        print("ingrese la posicion del numero que desea cambiar")
        print("fila: ")
        fila = int(input("->"))
        print("columna: ")
        columna = int(input("->"))
        print("ingrese el nuevo numero: ")
        numero = int(input("->"))
        matriz[fila][columna] = numero
        print("la matriz es: ")
        for i in range(5):
            for j in range(5):
                print(matriz[i][j], end=" ")
            print()

    else:
        print("la matriz se queda igual")

    def determinante(matriz):
        if len(matriz) == 1:
            return matriz[0][0]
        else:
            determinante = 0
            for i in range(len(matriz)):
                determinante += (-1)**i * matriz[0][i] * determinante([fila[:i] + fila[i+1:] for fila in (matriz[1:])])
            return determinante
    print("el determinante de la matriz es: ", determinante(matriz))
    print('\033[35m'+ "===================" + '\033[0m')

def main():
    print('\033[35m'+ "===================" + '\033[0m')
    print('\033[35m'+ "DETERMINANTE DE UNA MATRIZ DE 5X5" + '\033[0m')
    print('\033[35m'+ "===================" + '\033[0m')
    print("¿cómo desea calcular el determinante de la matriz?")
    print("1. de manera iterativa")
    print("2. de manera recursiva")
    opcion = int(input("->"))
    if opcion == 1:
        iterativo()
    elif opcion == 2:
        recursivo()
    else:
        print("opcion no valida")

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def agregar(self, dato):
        if self.inicio is None:
            self.inicio = self.fin = Nodo(dato)
        else:
            aux = self.fin
            self.fin = aux.siguiente = Nodo(dato)

    def recorrer(self):
        aux = self.inicio
        while aux:
            print(aux.dato, end=" ")
            aux = aux.siguiente
        print()

    def determinante(self):
        if self.inicio is None:
            return 0
        else:
            matriz = []
            aux = self.inicio
            while aux:
                matriz.append(aux.dato)
                aux = aux.siguiente
            if len(matriz) == 1:
                return matriz[0][0]
            else:
                determinante = 0
                for i in range(len(matriz)):
                    determinante += (-1)**i * matriz[0][i] * self.determinante([fila[:i] + fila[i+1:] for fila in (matriz[1:])])
                return determinante

    def cambiar(self):
        print("ingrese la posicion del numero que desea cambiar")
        print("fila: ")
        fila = int(input("->"))
        print("columna: ")
        columna = int(input("->"))
        print("ingrese el nuevo numero: ")
        numero = int(input("->"))
        aux = self.inicio
        while aux:
            if aux.dato[fila][columna] == aux.dato[fila][columna]:
                aux.dato[fila][columna] = numero
            aux = aux.siguiente

    def matriz(self):
        aux = self.inicio
        while aux:
            for i in range(5):
                for j in range(5):
                    print(aux.dato[i][j], end=" ")
                print()
            aux = aux.siguiente


if __name__ == "__main__":
    main()
    lista = Lista()
    for i in range(5):
        lista.agregar([])
        for j in range(5):
            lista.agregar(int(input("ingrese el numero de la posicion ["+str(i)+"]["+str(j)+"]: ")))
    print("la matriz es: ")
    lista.matriz()
    print('\033[36m'+"¿desea cambiar algún numero de la matriz? (si/no)"+'\033[0m')
    respuesta = input("->")
    if respuesta == "si":
        lista.cambiar()
        print("la matriz es: ")
        lista.matriz()
    else:
        print("la matriz se queda igual")
    print("el determinante de la matriz es: ", lista.determinante())


