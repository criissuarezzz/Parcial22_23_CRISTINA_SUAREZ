#dada la lista [18, 50, 210, 80, 145, 333, 70, 30], imprimir el numero en caso de que sea multiplo de 10 y menor de 200 utilizando clases y tda
class Lista:
    def __init__(self, lista):
        self.lista=lista

    def multiplo(self):
        for i in self.lista:
            if i%10==0 and i<200:
                print("El número", i, "es multiplo de 10 y menor de 200")
            if i>300:
                print("El numero", i ,"es mayor de 300, paramos el programa")
                break

    def mezcla(lista):
        if len(lista)<=1:
            return lista
        else:
            medio=len(lista)//2
            izquierda=mezcla(lista[:medio])
            derecha=mezcla(lista[medio:])
            return mezcla(izquierda, derecha)

#puesto a prueba:
print("Mezcla:")
print(mezcla([11,3,81,7,45]))
lista=Lista([18, 50, 210, 80, 145, 333, 70, 30])
lista.multiplo()

