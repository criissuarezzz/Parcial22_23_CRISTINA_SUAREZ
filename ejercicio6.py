def determinante():
    matriz = []
    for i in range(5):
        matriz.append([])
        for j in range(5):
            matriz[i].append(int(input("Introduce el valor de la posición (" + str(i) + "," + str(j) + "): ")))
    print("La matriz es: ")
    for i in range(5):
        print(matriz[i])


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
        print("la matriz ahora es: ")
        for i in range(5):
            print(matriz[i])
    else:
        print("la matriz no se modificará")
    print('\033[36m'+"¿desea calcular el determinante de manera iterativa o recursiva? (iterativa/recursiva)"+'\033[0m')
    respuesta = input("->")
    if respuesta == "iterativa":
        print('\033[35m'+ "DETERMINANTE DE UNA MATRIZ 5X5 DE MANERA ITERATIVA " + '\033[0m')
        determinante=matriz[0][0]*matriz[1][1]*matriz[2][2]*matriz[3][3]*matriz[4][4]+matriz[0][1]*matriz[1][2]*matriz[2][3]*matriz[3][4]*matriz[4][0]+matriz[0][2]*matriz[1][3]*matriz[2][4]*matriz[3][0]*matriz[4][1]+matriz[0][3]*matriz[1][4]*matriz[2][0]*matriz[3][1]*matriz[4][2]+matriz[0][4]*matriz[1][0]*matriz[2][1]*matriz[3][2]*matriz[4][3]-matriz[0][4]*matriz[1][3]*matriz[2][2]*matriz[3][1]*matriz[4][0]-matriz[0][3]*matriz[1][2]*matriz[2][1]*matriz[3][0]*matriz[4][4]-matriz[0][2]*matriz[1][1]*matriz[2][0]*matriz[3][4]*matriz[4][3]-matriz[0][1]*matriz[1][0]*matriz[2][4]*matriz[3][3]*matriz[4][2]-matriz[0][0]*matriz[1][4]*matriz[2][3]*matriz[3][2]*matriz[4][1]
        print("el determinante de la matriz es: ", determinante)
    elif respuesta == "recursiva":
        print('\033[35m'+ "DETERMINANTE DE UNA MATRIZ 5X5 DE MANERA RECURSIVA " + '\033[0m')
        def determinante(matriz):
            if len(matriz) == 1:
                return matriz[0][0]
            else:
                determinante = 0
                for i in range(len(matriz)):
                    determinante += (-1)**i * matriz[0][i] * determinante([fila[:i] + fila[i+1:] for fila in (matriz[1:])])
                return determinante
        print("el determinante de la matriz es: ", determinante(matriz))
    else:
        print("opcion no valida")
        interorecur()

if __name__=="__main__":
    determinante()