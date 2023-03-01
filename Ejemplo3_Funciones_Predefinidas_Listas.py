"""
Funciones predefinidas para las Listas.

"""
lista_numeros = [9, 5, 7, 2, 1, 3, 4, 6, 10]
lista_equipos = ['Boca', 'River', 'Velez', 'Lanus', 'Racing']


# Ordenar lista con                                                                  .sort().
lista_numeros.sort()
print(lista_numeros)

# Añadir elementos al final de la lista con                                          .append("elemento").

lista_numeros.append(14)
print(lista_numeros)


# Añadir elementos en posicion especifica con                                        .insert(indice,"elemento").

lista_numeros.insert(5,'Agregue un valor')
print(lista_numeros)

# Eliminar elemento por indice con                                                   .pop(indice).


lista_numeros.pop(5)
print(lista_numeros)

# Eliminar elemento especifico por valor con                                         .remove("elemento").


lista_numeros.remove(7)
print(lista_numeros)

# Dar vuelta una lista con                                                           .reverse().


lista_numeros.reverse()
print(lista_numeros)

# Contar elementos con                                                               .len(lista).


len(lista_numeros)
print(lista_numeros)

# Saber si se encuentra un elemento por su valor con                                 print("elemento" in lista) da valor booleano.

print("Boca" in lista_equipos)


# Saber cuantas veces se repite un elemento con                                      .count("elemento").

lista_numeros.count(1)
print(lista_numeros)


# Conseguir elemento a partir de su indice con                                       .index("elemento").

lista_numeros.index(10)
print(lista_numeros)


# Concatenación de listas con                                                        .exted(lista a unir).


lista_numeros.extend(lista_equipos)
print(lista_numeros)

