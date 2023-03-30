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
    


lista=Lista([18, 50, 210, 80, 145, 333, 70, 30])
lista.multiplo()
print("La lista ordenada es: ", lista.mezcla([18, 50, 210, 80, 145, 333, 70, 30]))


