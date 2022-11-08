from arbol import (
    nodoArbol,
    insertar_nodo,
    mostrar_datos_star_wars,
    inorden_metros_star_wars,
    inorden_peso_star_wars,
    contar_heroes,
    eliminar_nodo,
    por_nivel,
    inorden,
    postorden,
    crear_bosque,
    arbol_vacio,
    busqueda,
)
arbol = nodoArbol()

lista = [
    ['Darrth Vader', 170, 60],
    ['Luke Skywalker', 150, 70],
    ['Leia Organa', 153, 65],
    ['Obi-Wan Kenobi', 180, 80],
    ['Han solo', 190, 90],
    ['Yoda', 70, 50],
    ['Kylo Ren', 190, 95],
    ['Palpatine', 186, 83],
    ['Chewbacca', 250, 130],
    ['R2-D2', 60, 70],
    ['Padmé Amidala', 156, 80],
    ['Qui-Gon Jinn', 193, 74],
    ['Grogu', 186, 86],
    ['Poe Dameron', 184, 83],
    ['Jabba el Hutt', 130, 300],
    ['Lando Calrissian', 150, 53],
    ['Jyn Erso', 160, 70],
    ['Conde Dooku', 190, 93],
    ['Jar Jar Binks', 240, 150],
    ['Mandalorian', 194, 82],
]

for nombre, altura, peso in lista:
    datos = {'altura': altura,
             'peso': peso}
    
    insertar_nodo(arbol, nombre, datos)

nuevo=input('Inserte el nombre  del nuevo personaje: ')
insertar_nodo(arbol,nuevo,False)

darBaja=input('Ingrese el nombre del personaje que desee dar de baja: ')
pos=eliminar_nodo(arbol,darBaja)
if pos:
    print('se ha eliminado correctamente')
else:
    print('no se ha encontrado ese personaje')

clave = input('ingrese nombre del personaje que desea modificar ')
modificar = eliminar_nodo(arbol, clave)
if modificar:
    name = input('ingrese el nuevo nombre ')
    insertar_nodo(arbol, name, False)
else:
     print('El personaje no se ha encontrado')
print()
print('Datos de Yoda,Mandalorian y Luke Skywalker')
mostrar_datos_star_wars(arbol,'Yoda')
mostrar_datos_star_wars(arbol,'Mandalorian')
mostrar_datos_star_wars(arbol,'Luke Skywalker')
print()
print('Personajes que miden menos de 0.9 metros: ')
inorden_metros_star_wars(arbol)
print()
print('Personajes que pesan mas de 75 kilos: ')
inorden_peso_star_wars(arbol)
print()
print('listado por nivel de los personajes')
por_nivel(arbol)

print()
print('¿Grogu esta en el arbol?')
buscar=busqueda(arbol,'Grogu')
if buscar:
    mostrar_datos_star_wars(arbol,'Grogu',arbol['altura'])
    
#print(inorden(arbol))

