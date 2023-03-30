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
    
    def mezcla(self, lista):
        if len(lista)>1:
            mitad=len(lista)//2
            izquierda=lista[:mitad]
            derecha=lista[mitad:]
            self.mezcla(izquierda)
            self.mezcla(derecha)
            i=0
            j=0
            k=0
            while i<len(izquierda) and j<len(derecha):
                if izquierda[i]<derecha[j]:
                    lista[k]=izquierda[i]
                    i+=1
                else:
                    lista[k]=derecha[j]
                    j+=1
                k+=1
            while i<len(izquierda):
                lista[k]=izquierda[i]
                i+=1
                k+=1
            while j<len(derecha):
                lista[k]=derecha[j]
                j+=1
                k+=1
        return lista
    #Dada la lista anterior y un valor 145 devolver el índice de 145 en la lista si 145 está en la lista, y −1 si 145 no está en la lista
    def indice(self, valor):
        for i in self.lista:
            if i==valor:
                print("El indice del valor", valor, "es", self.lista.index(valor))
            else:
                print("El valor", valor, "no está en la lista. -1")

lista=Lista([18, 50, 210, 80, 145, 333, 70, 30])
lista.multiplo()
print("La lista ordenada es: ", lista.mezcla([18, 50, 210, 80, 145, 333, 70, 30]))
lista.indice(145)