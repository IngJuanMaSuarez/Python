from vector import Vector
import random

class Matriz():
    
    def __init__(self, filas, columnas, valor = None):
        self.dato = Vector(filas)
        for fila in range(filas):
            self.dato[fila] = Vector(columnas, valor)

    def get_alto(self):
        return len(self.dato)

    def get_ancho(self):
        return len(self.dato[0])

    def __getitem__(self, indice):
        return self.dato[indice]

    def __str__(self):
        result = ""

        for fila in range(self.get_alto()):
            for columna in range(self.get_ancho()):
                result += str(self.dato[fila][columna]) + " "

            result += "\n"

        return str(result)

    #Metodo para poblar la Matriz con numeros aleatorios
    def __setrandomnumber__(self):
      for fila in range(self.get_alto()):
          for columna in range(self.get_ancho()):
              self.dato[fila][columna] = random.randint(0, 100)

"""
Crear una objeto de la clase Matriz y explorar sus metodos
"""

matriz = Matriz(3, 3)
print(matriz)

for fila in range(matriz.get_alto()):
  for columna in range(matriz.get_ancho()):
    matriz[fila][columna] = fila * columna
print(matriz)

print(matriz.get_alto())
print(matriz.get_ancho())
print(matriz.__getitem__(2)[1])

matriz.__setrandomnumber__()
print(matriz)