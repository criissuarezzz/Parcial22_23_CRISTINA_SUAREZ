import unittest
import ejercicio4 as Alumno

class TestAlumno(unittest.TestCase):
    def test_alumno(self):
        alumno1=Alumno("Pedro", 5)
        self.assertEqual(alumno1.__str__(), "Nombre: Pedro. Nota: 5.")
        alumno2=Alumno("Juan", 6.3)
        self.assertEqual(alumno2.__str__(), "Nombre: Juan. Nota: 6.3.")
        alumno3=Alumno("Ana", 4.2)
        self.assertEqual(alumno3.__str__(), "Nombre: Ana. Nota: 4.2.")

if __name__ == '__main__':
    unittest.main()