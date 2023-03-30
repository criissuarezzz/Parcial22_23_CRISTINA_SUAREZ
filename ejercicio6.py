def sarrus5x5iterativo():
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



if __name__ == "__main__":
    sarrus5x5iterativo()
