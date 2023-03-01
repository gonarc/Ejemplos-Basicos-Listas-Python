"""
Listas Multidimensionales: Son listas dentro de listas donde la lista de afuera es la primera dimensión y se cuenta hacía dentro.
ej: listaPrimeraDimension= 

[primera dimension
[segunda dimension [tercera dimension] ] ]
"""
contactos = [
    [
        'gonzalo',
        'gonzalo@gonzalo.com'
    ],
    [
        'maximiliano',
        'maximiliano@maximiliano.com'
    ],
    [
        'sol',
        'sol@sol.com'
    ],
    [
        'maria',
        'maria@maria.com'
    ],
    [
        'juan',
        'juan@juan.com'
    ]

]

print(contactos[0])  # 'gonzalo',
# 'gonzalo@gonzalo.com'


print(contactos[0][1])  # 'gonzalo@gonzalo.com'

# Recorrer Lista completa con un ciclo FOR
print("")
print("***********Recorrer Lista completa****************")
print("")
for contador in contactos:
    print(contador)

# Recorrer Lista Elemento especifico con un ciclo FOR
print("")
print("***********Recorrer Lista Elemento especifico****************")
print("")

for contador in contactos:
    print(contador[1])

# Recorrer Lista y Elemento con un ciclo FOR
print("")
print("***********Recorrer Lista y Elemento****************")
print("")
for contador in contactos:
    print("")
    for elemento in contador:
        print(elemento)
