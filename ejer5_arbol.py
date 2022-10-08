from arbol import (
    nodoArbol,
    insertar_nodo,
    inorden_villano,
    inorden_empieza_con,
    contar_heroes,
    eliminar_nodo,
    inorden,
    postorden,
    postorden_heroes,
    crear_bosque,
    arbol_vacio,
    contar_heroes_villanos,
    busqueda,
)

arbol = nodoArbol()


heroes = nodoArbol()
villanos = nodoArbol()


lista = [
    ['iron man', False, 1960],
    ['capitana marvel', False, 1890],
    ['thor', False, 1962],
    ['dotor strange', False, 1961],
    ['thanos', True, 1962],
    ['red skull', True, 1963],
    ['capitan america', False, 2000],
]

for nombre, villano, anio in lista:
    datos = {'villano': villano,
             'anio_aparicion': anio}
    
    insertar_nodo(arbol, nombre, datos)

#inorden_heroes_villanos(arbol)
print('B')
inorden_villano(arbol)
print()
print('C')
inorden_empieza_con(arbol, 'c')
print()
print('D')
print('La cantidad de superheroes que hay en el arbol es: ')
print(contar_heroes(arbol))
print()
print('F')
postorden(arbol)
print('G')
print('superheroes')
#postorden_heroes(arbol)
crear_bosque(arbol, heroes, villanos)

cantidad = {'villanos': 0, 'heroes': 0}
contar_heroes_villanos(arbol, cantidad)
print('cantidad de heroes y villanos', cantidad)


print('heroes')
inorden(heroes)

print()
print('villanos')
inorden(villanos)
print()
print('E')
clave = input('ingrese parte de lo que desea buscar ')
inorden_empieza_con(arbol, clave)
print()
clave = input('ingrese nombre que desea modificar ')
pos = eliminar_nodo(arbol, clave)
if pos:
    name = input('ingrese nuevo nombre ')
    insertar_nodo(arbol, name, False)
else:
     print('valor no encontrado en el arbol')

inorden(arbol)
print()