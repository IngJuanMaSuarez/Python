class Nodo():
  def __init__(self, dato, siguiente):
    self.dato = dato
    self.siguiente = siguiente

"""
Crear varios objetos nodos usando la clase Nodo
"""

nodo1 = None
nodo2 = Nodo("A", None)
nodo3 = Nodo("B", nodo2)

print(nodo1)
print(nodo2)
print(nodo2.dato)
print(nodo2.siguiente)
print(nodo3.dato)
print(nodo3.siguiente)
print(nodo3.siguiente.dato)

cabeza = None

for numero in range(1, 6):
  cabeza = Nodo(numero, cabeza)

while cabeza != None:
  print(cabeza.dato)
  cabeza = cabeza.siguiente