#implementar sobre el TDA polinomio de la clase anterior, los siguientes métodos:
#restar
#dividir
#eliminar un termino
#determinar si un termino existe

class datoPolinomio:
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente

class nodoPolinomio:
    def __init__(self, dato, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente

class Polinomio:
    def __init__(self):
        self.termino_mayor = None
        self.grado= -1

    def agregar_termino(self, coeficiente, exponente):
        if self.termino_mayor is None:
            self.termino_mayor = nodoPolinomio(datoPolinomio(coeficiente, exponente))
            self.grado = exponente
        else:
            aux = self.termino_mayor
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = nodoPolinomio(datoPolinomio(coeficiente, exponente))
            if exponente > self.grado:
                self.grado = exponente

    def mostrar(self):
        aux = self.termino_mayor
        while aux is not None:
            print(aux.dato.coeficiente, "x^", aux.dato.exponente, end=" ")
            aux = aux.siguiente
        print()

    def evaluar(self, x):
        if self.termino_mayor is None:
            print("El polinomio no tiene terminos")
        else:
            aux = self.termino_mayor
            resultado = 0
            while aux is not None:
                resultado += aux.dato.coeficiente * (x ** aux.dato.exponente)
                aux = aux.siguiente
            return resultado
        
    def restar(self, polinomio):
        if self.termino_mayor is None:
            print("El polinomio no tiene terminos")
        else:
            aux = self.termino_mayor
            while aux is not None:
                aux.dato.coeficiente -= polinomio.evaluar(aux.dato.exponente)
                aux = aux.siguiente
    
    def dividir(self, polinomio):
        if self.termino_mayor is None:
            print("El polinomio no tiene terminos")
        else:
            aux = self.termino_mayor
            while aux is not None:
                aux.dato.coeficiente /= polinomio.evaluar(aux.dato.exponente)
                aux = aux.siguiente
    
    def eliminar_termino(self, exponente):
        if self.termino_mayor is None:
            print("El polinomio no tiene terminos")
        else:
            aux = self.termino_mayor
            while aux is not None:
                if aux.dato.exponente == exponente:
                    aux.dato.coeficiente = 0
                aux = aux.siguiente

    def existe_termino(self, exponente):
        if self.termino_mayor is None:
            print("El polinomio no tiene terminos")
        else:
            aux = self.termino_mayor
            while aux is not None:
                if aux.dato.exponente == exponente:
                    return True
                aux = aux.siguiente
            return False
        
    def mostrar_grado(self):
        print(self.grado)


p1 = Polinomio()
p1.agregar_termino(2, 3)
p1.agregar_termino(3, 2)
p1.agregar_termino(4, 1)
p1.agregar_termino(5, 0)
print("El polinomio 1 es:")
p1.mostrar()
print("cuyo grado es: ")
p1.mostrar_grado()
print("Si eliminamos el termino de grado 2, el polinomio queda: ")
p1.eliminar_termino(2)

p2 = Polinomio()
p2.agregar_termino(2, 3)
p2.agregar_termino(3, 2)
p2.agregar_termino(4, 1)
p2.agregar_termino(5, 0)
print("El polinomio 2 es:")
p2.mostrar()
print("cuyo grado es: ")
p2.mostrar_grado()
print("Si eliminamos el termino de grado 3, el polinomio queda: ")
p2.eliminar_termino(3)

p3 = Polinomio()
p3.agregar_termino(2, 3)
p3.agregar_termino(3, 2)
p3.agregar_termino(4, 1)
p3.agregar_termino(5, 0)
print("El polinomio 3 es:")
p3.mostrar()
print("cuyo grado es: ")
p3.mostrar_grado()
print("Si eliminamos el termino de grado 4, el polinomio queda: ")
p3.eliminar_termino(4)

print("Si al polinomio 1 le restamos el polinomio 2, el resultado es: ")
p1.restar(p2)
print("Si al polinomio 2 le restamos el polinomio 1, el resultado es: ")
p2.restar(p1)
print("Si al polinomio 3 le restamos el polinomio 1, el resultado es: ")
p3.restar(p1)

print("Si el polinomio 1 lo dividimos por el polinomio 2, el resultado es: "+ p1.dividir(p2))
print("Si el polinomio 2 lo dividimos por el polinomio 1, el resultado es: "+ p2.dividir(p1))
print("Si el polinomio 3 lo dividimos por el polinomio 1, el resultado es: "+ p3.dividir(p1))

print("¿Existe el termino de grado 2 en el polinomio 1? "+ p1.existe_termino(2))
print("¿Existe el termino de grado 3 en el polinomio 1? "+ p1.existe_termino(3))
print("¿Existe el termino de grado 4 en el polinomio 1? "+ p1.existe_termino(4))