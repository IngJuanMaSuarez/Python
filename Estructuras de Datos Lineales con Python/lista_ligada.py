from nodo import Nodo

class ListaLigada:
  def __init__(self):
    self.cabeza = None
    self.tamano = 0

  def unir(self, dato):
    nodo = Nodo(dato, None)

    if self.cabeza == None:
      self.cabeza = nodo
    else:
      posicion_actual = self.cabeza

      while posicion_actual.siguiente:
        posicion_actual = posicion_actual.siguiente

      posicion_actual.siguiente = nodo

    self.tamano += 1

  def calcular_tamano(self):
    return str(self.tamano)

  def iterar(self):
    posicion_actual = self.cabeza

    while posicion_actual:
      valor = posicion_actual.dato
      posicion_actual = posicion_actual.siguiente
      yield valor

  def borrar(self, dato):
    posicion_actual = self.cabeza
    anterior = self.cabeza

    while posicion_actual:
      if posicion_actual.dato == dato:
        if posicion_actual == self.cabeza:
          self.cabeza = posicion_actual.siguiente
        else:
          anterior.siguiente = posicion_actual.siguiente
          self.tamano -= 1
          return posicion_actual.dato
      anterior = posicion_actual
      posicion_actual = posicion_actual.siguiente

  def buscar(self, dato):
    for nodo in self.iterar():
      if dato == nodo:
        print("Dato", dato, "encontrado")

  def limpiar(self):
    self.cabeza = None
    self.tamano = 0

"""
Crear listas usando la clase
"""

print("Lista Ligada")
palabras = ListaLigada()

palabras.unir("huevo")
palabras.unir("jamon")
palabras.unir("leche")

posicion_actual = palabras.cabeza

while posicion_actual:
  print(posicion_actual.dato)
  posicion_actual = posicion_actual.siguiente

for palabra in palabras.iterar():
  print(palabra)

palabras.buscar("leche")

palabras.buscar("chocolate")

palabras.limpiar()

for palabra in palabras.iterar():
  print(palabra)