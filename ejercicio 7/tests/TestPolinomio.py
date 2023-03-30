import unittest
from ejercicio7 import Polinomio
class TestPolinomio(unittest.TestCase):
    def test_agregar_termino(self):
        p1=Polinomio()
        p1.agregar_termino(2,-4)
        p1.agregar_termino(3,2)
        self.assertEqual(p1.mostrar_polinomio(), "+2x^3-4x^2")
    
    def test_modificar_termino(self):
        p1=Polinomio()
        p1.agregar_termino(2,-4)
        p1.agregar_termino(3,2)
        p1.modificar_termino(2,2)
        self.assertEqual(p1.mostrar_polinomio(), "+2x^3+2x^2")
    
    def test_eliminar_termino(self):
        p1=Polinomio()
        p1.agregar_termino(2,-4)
        p1.agregar_termino(3,2)
        p1.eliminar_termino(3)
        self.assertEqual(p1.mostrar_polinomio(), "-4x^2")
    
    def test_mostrar_polinomio(self):
        p1=Polinomio()
        p1.agregar_termino(2,-4)
        p1.agregar_termino(3,2)
        self.assertEqual(p1.mostrar_polinomio(), "+2x^3-4x^2")
    
    def test_evaluar_polinomio(self):
        p1=Polinomio()
        p1.agregar_termino(2,-4)
        p1.agregar_termino(3,2)
        self.assertEqual(p1.evaluar_polinomio(4), 64)
    
    def test_existe_termino(self):
        p1=Polinomio()
        p1.agregar_termino(2,-4)
        p1.agregar_termino(3,2)
        self.assertEqual(p1.existe_termino(2), True)
    
    def test_dividir_polinomios(self):
        p1=Polinomio()
        p1.agregar_termino(2,-4)
        p1.agregar_termino(3,2)
        p2=Polinomio()
        p2.agregar_termino(3,4)
        p2.agregar_termino(4,2)
        self.assertEqual(p1.dividir_polinomios(p2), "El polinomio 1 no es divisible entre el polinomio 2")

if __name__ == '__main__':
    unittest.main()
