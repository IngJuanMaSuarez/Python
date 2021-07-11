import random

class Vector:

    #Metodo constructor
    def __init__(self, tamano, valor = None):

        self.tamano = tamano

        #Los items se van a guardar en una lista vacia
        self.items = list()
        for i in range(self.tamano):
            self.items.append(valor)

    #Metodo privado (solo consulta) para conocer su tamano
    def __len__(self):
        return len(self.items)

    #Representar en string los elementos
    def __str__(self):
        return str(self.items)

    #Iterador para recorrer la estructura, asignar valores o cambiarlos
    def __iter__(self):
        return iter(self.items)

    #Obtener un elemento particular del Vector (get)
    def __getitem__(self, indice):
        return self.items[indice]

    #Metodo para reemplazar elementos (set)
    def __setitem__(self, indice, nuevo_valor):
        self.items[indice] = nuevo_valor

    #Metodo para poblar el Vector con numeros aleatorios
    def setrandomnumber(self):
      for i in range(self.tamano):
        self.items[i] = random.randint(0, 100)

    #Metodo que suma todos los valores del Vector
    def sumaitems(self):
        suma = 0
        for i in range(self.tamano):
            suma += self.items[i]
        return suma

"""
Crear una objeto de la clase Vector y explorar sus metodos
"""

vector = Vector(10)
vector.setrandomnumber()

print(vector)
print(vector.__len__())
print(vector.__str__())
print(vector.__getitem__(3))

vector.__setitem__(3, 500)
print(vector.__getitem__(3))
print(vector)

print(vector.sumaitems())