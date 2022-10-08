from arbol import (
    nodoArbol,
    insertar_nodo,
    inorden_criaturas,
    inorden_mostrar_datos,
    inorden_empieza_con,
    contar_heroes,
    inorden_mostrar_criaturas_derrocadas_por,
    eliminar_nodo,
    inorden,
    inorden_contiene,
    postorden,
    postorden_heroes,
    crear_bosque,
    arbol_vacio,
    contar_heroes_villanos,
    busqueda,
    por_nivel,
    inorden_capturadas_por,
    inorden_dic,
    inorden_criaturas_completo,
)

arbol = nodoArbol()


heroes = nodoArbol()
villanos = nodoArbol()


lista = [
    ['Ceto', '-','  ',' '], ['Cerda de Cromión', 'Teseo','  ',' '],
    ['Tifon', 'Zeus',' ', ' '], ['Ortro', 'Heracles',' ',' '],
    ['Equidna', 'Argos Panoptes',' ', ' ' ], ['Toro de Creta', 'Teseo',' ',' '],
   # ['Dino', '-',' ',' ' ], ['Jabalí de Calidón', 'Atalanta',' ',' ' ],
    #['Pefredo', '-',''], ['Carcinos', '-',''],
    #['Enio', '-',' '], ['Gerión', 'Heracles',''],
    #['Escila', '-',''], ['Cloto', '-',''],
    #['Caribdis', '-',''], ['Láquesis', '-',''],
    #['Euríale', '-',''], ['Átropos', '-',''],
    #['Esteno', '-',''], ['Minotauro de Creta', '-',''],
    #['Medusa', 'Perseo',''], ['Harpías', '-',''],
    ['Ortro', 'Heracles',' ',' '],['Ladón', 'Heracles',' ',' '],['Argos Panoptes', 'Hermes',' ',' '],
    ['Águila del Cáucaso', '-','',''],['Aves del Estínfalo', '-','',''],
    #['Quimera', 'Belerofonte',''],
    ['Talos', 'Medea','',''],
    #['Hidra de Lerna', 'Heracles',''],
    ['Sirenas', '-',' ',' '],
    #['León de Nemea', 'Heracles',''],
    #['Pitón', 'Apolo',''],
    #['Esfinge', 'Edipo',''],
    ['Cierva de Cerinea', '-',' ',' '],
    #['Dragón de la Cólquida', '-',''],
    ['Basilisco', '-',' ',' '],
    ['Cerbero', '-',' ', ' '],
    ['Jabalí de Erimanto', '-',' ',' '],


]

for criatura, derrotadoPor, descripcion,capturada in lista:
    datos = {'Derrotado por': derrotadoPor,
     'Breve descripcion':None,
     'Capturada':None}
    insertar_nodo(arbol,criatura,datos)
print("A")
inorden_criaturas(arbol) #A

print("B")
clave = input('ingrese la criatura que quiere agregarle la descripcion ')#B
busq=busqueda(arbol,clave)

if busq:
    pos = eliminar_nodo(arbol, clave)
    if pos:
        name = input('ingrese el nombre de la criatura ')
        derrotado= input('ingrese por quien fue derrotado ')
        descripcion=input('ingrese la descripcion')
        datos={'Derrotado por': derrotado,'Breve descripcion': descripcion, 'Capturada': None}
        insertar_nodo(arbol, name, datos)
else:
    print('La criatura no se encuentra en el arbol')

inorden_criaturas_completo(arbol)
print()
print("C")
clave='Talos'
inorden_mostrar_datos (arbol,clave) #C
print()
print("D")
dioses=dict()#D
inorden_dic(arbol,dioses)
mayor_derrotas= ''
var=0
for i in dioses:   
    if(i != '-' and dioses.get(i) > var):
         mayor_derrotas=i
         var=dioses.get(i)
        
    #print(i,dioses.get(i))

print('Dios con mayor de derrotas:')
print(mayor_derrotas)
print("E")
print('Criaturas derrotadas por Heracles')#E
inorden_mostrar_criaturas_derrocadas_por(arbol,'Heracles')
print()
print("F")
print('Criaturas que no han sido derrotadas')#F
inorden_mostrar_criaturas_derrocadas_por(arbol,'-')
print()
print("H")
pos = eliminar_nodo(arbol, 'Toro de Creta')#H
if pos:
    datos={'Derrotado por ': '-','Breve descripcion ': ' ','Capturada':'Heracles'}
    insertar_nodo(arbol, 'Toro de Creta', datos)

pos = eliminar_nodo(arbol, 'Cierva de Cerinea')
if pos:
    datos={'Derrotado por ': '-','Breve descripcion ': ' ','Capturada':'Heracles'}
    insertar_nodo(arbol, 'Cierva de Cerinea', datos)

pos = eliminar_nodo(arbol, 'Cerbero')
if pos:
    datos={'Derrotado por ': '-','Breve descripcion ': ' ','Capturada':'Heracles'}
    insertar_nodo(arbol, 'Cerbero', datos)

pos = eliminar_nodo(arbol, 'Jabalí de Erimanto')
if pos:
    datos={'Derrotado por ': '-','Breve descripcion ': ' ','Capturada':'Heracles'}
    insertar_nodo(arbol, 'Jabalí de Erimanto', datos)
inorden_criaturas_completo(arbol)
print()

print("I")
clave = input('ingrese parte de lo que desea buscar ')#I
inorden_contiene(arbol, clave)
print()
print("J")
eliminar_nodo(arbol,'Basilisco')#J
eliminar_nodo(arbol,'Sirenas')#J

inorden_criaturas_completo(arbol)
print()
print("K")
pos = eliminar_nodo(arbol, 'Aves del Estínfalo')#K
if pos:
    datos={'Derrotado por ': 'Heracles','Breve descripcion ': ' ','Capturada':''}
    insertar_nodo(arbol, 'Aves del Estínfalo', datos)
print()
print("L")

pos = eliminar_nodo(arbol, 'Ladón')#L
if pos:
    datos={'Derrotado por ': 'Heracles','Breve descripcion ': ' ','Capturada':''}
    insertar_nodo(arbol, 'Dragón Ladón', datos)
inorden_criaturas_completo(arbol)

print()
print("M")
por_nivel(arbol)#M

print()
print("N")
print('criaturas capturadas por heracles')#N
inorden_capturadas_por(arbol,'Heracles')   