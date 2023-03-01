"""
Listas: Son secuencias ordenadas que guardan una variedad de tipos de datos bajo un nombre especifico.

* Son mutables.

* Se utilizan corchetes[] y comas para separar [1,2,3].

* Se puede utilizar la funcion list() para hacer una lista (debe tener dentro una TUPLA ()
para que pueda ser invocado correctamente) y permite colocar una funcion dentro. ej: 
years= list(range(0,11)) 
print(years) # [1,2,3,4,5,6,7,8,9,10].

* Soportan INDICES Y SLICING.

* Pueden haber listas dentro de listas y pueden guardar metodos que pueden ser llamados.

"""

years= list(range(0,11)) 
print(years) # [1,2,3,4,5,6,7,8,9,10]
print("Indices")

#Indices

lista=['Gonzalo',1,5,'Arce','maxi',9,41]
print(lista)

#
print(lista[5]) # 9
print(lista[-1]) # 9 (De adelante para atrás)
print(lista[4]) # 'maxi'

print("Slicing")

#Slicing
print(lista[1:4]) # [1,5,'Arce']
print(lista[1:]) # [1,5,'Arce','maxi',9,41]

#Reemplazo de valor en una lista
print("Reemplazo de valor en una lista")

lista[0] = "Ezequiel"
print(lista)

print("")
print("")

#Iteracion de una lista con For.
for contador in lista:
    print(contador)
print("")

#iteracion con enumeracion de datos
for contador in lista:
    print(f"{lista.index(contador)+1} - {contador}")
 
    
#Agregar datos pedidos al usuario a una lista.
print("")
print("############# EQUIPOS DE FUTBOL ###########")
print("")
equipos_de_futbol=['Boca','River','Independiente','Racing']
for equipo in equipos_de_futbol:
    print(f"{equipos_de_futbol.index(equipo)+1} - {equipo}")
    
#Agregar equipos con While y append():
nuevos_equipos=""
while nuevos_equipos != "fin":
    nuevos_equipos= input("Ingrese el nuevo equipo: ")
    # If para que el elemento parar no se agregue a la lista.
    if nuevos_equipos != "fin":
      equipos_de_futbol.append(nuevos_equipos)
    
for equipo in equipos_de_futbol:
    print(f"{equipos_de_futbol.index(equipo)+1} - {equipo}")
