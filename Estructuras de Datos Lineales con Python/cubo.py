from vector import Vector
import random

class Cubo:

    def __init__(self, filas, columnas, profundidad, valor = None):
        self.dato = Vector(filas)
        for fila in range(filas):
            self.dato[fila] = Vector(columnas)
            for columna in range(columnas):
                self.dato[fila][columna] = Vector(profundidad, valor)

    def get_alto(self):
        return len(self.dato)

    def get_ancho(self):
        return len(self.dato[0])

    def get_profundidad(self):
        return len(self.dato[0][0])

    def __str__(self):
        result = ""

        for fila in range(self.get_alto()):
            for columna in range(self.get_ancho()):
                for fondo in range(self.get_profundidad()):
                    result += str(self.dato[fila][columna][fondo]) + " "

                result += "\n"
            result += "\n"

        return str(result)

    #Metodo para poblar el Cubo con numeros aleatorios
    def __setrandomnumber__(self):
      for fila in range(self.get_alto()):
          for columna in range(self.get_ancho()):
              for fondo in range(self.get_profundidad()):
                  self.dato[fila][columna][fondo] = random.randint(0, 100)

"""
Se crea un objeto rubik de la clase Cubo y se exploran los metodos
"""

rubik = Cubo(2, 3, 4)
print(rubik)

print(rubik.get_alto())
print(rubik.get_ancho())
print(rubik.get_profundidad())

rubik.__setrandomnumber__()
print(rubik)