# Hacer una función que genere una lista de diccionarios que contengan id y edad,
# donde edad sea un número aleatorio entre 1 y 100 y la longitud de la lista sea de 10 elementos.
# retornar la lista.

import random

def listDicGenerator():
  diccionario = {}
  ids = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
  listaDeDiccionarios = []
  for i in ids:
      diccionario['id'] = i
      diccionario['edad'] = random.randint(1, 100)
      listaDeDiccionarios.append(diccionario.copy())
  return listaDeDiccionarios

print(listDicGenerator())

# Hacer otra función que reciba lo generado en la primer función y ordenarlo de mayor a menor.
# Printear el id de la persona más joven y más vieja.
# Devolver la lista ordenada.
