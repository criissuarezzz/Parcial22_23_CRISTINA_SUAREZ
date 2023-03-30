def sarrusiterativo():
    print('\033[35m'+ "DETERMINANTE DE UNA MATRIZ 5X5 DE MANERA ITERATIVA " + '\033[0m')
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
