from lista_2 import Lista
from random import randint, choice
#Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, 
# cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. 
# Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver 
#las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
#a. obtener la cantidad de Pokémons de un determinado entrenador;
#b. listar los entrenadores que hayan ganado más de tres torneos;
#[115]
#c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
#d. mostrar todos los datos de un entrenador y sus Pokémos;
#e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
#f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
#(tipo y subtipo);
#g. el promedio de nivel de los Pokémons de un determinado entrenador;
#h. determinar cuántos entrenadores tienen a un determinado Pokémon;
#i. mostrar los entrenadores que tienen Pokémons repetidos;
#j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
#k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador 
#como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se 
#deberán mostrar los datos de ambos

lista_entrenadores = Lista()

class Entrenador():

    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas

    def __str__(self):
        return f'{self.nombre}'
        # - {self.torneos_ganados} - {self.batallas_perdidas} - {self.batallas_ganadas}'
class Pokemon():
 
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f'{self.nombre} - {self.nivel} - {self.tipo} - {self.subtipo}'
dic_entrenadores = [
    {'nombre': 'Roman', 'torneos_ganados': 10, 'batallas_perdidas': 1, 'batallas_ganadas': 9},
    {'nombre': 'Lidia', 'torneos_ganados': 6, 'batallas_perdidas': 2, 'batallas_ganadas': 4},
    {'nombre': 'Susana', 'torneos_ganados': 2, 'batallas_perdidas': 0, 'batallas_ganadas': 2},
    {'nombre': 'Jose', 'torneos_ganados': 6, 'batallas_perdidas': 5, 'batallas_ganadas': 1},
    {'nombre': 'Pedro', 'torneos_ganados': 5, 'batallas_perdidas': 4, 'batallas_ganadas': 1},
        ]
dic_pokemones = [
    {'nombre': 'pikachu', 'nivel': 2, 'tipo': 'electrico', 'subtipo': 'ninguno '},
    {'nombre': 'Charmeleon', 'nivel': 4, 'tipo': 'fuego', 'subtipo': 'planta'},
    {'nombre': 'Charizard', 'nivel': 5, 'tipo': 'fuego', 'subtipo': 'volador'},
    {'nombre': 'Squirtle', 'nivel': 1, 'tipo': 'agua', 'subtipo': 'ninguno'},
    {'nombre': 'Wingull', 'nivel': 3, 'tipo': 'agua', 'subtipo': 'volador'},
        ]


for entrenador in dic_entrenadores:
    lista_entrenadores.insertar(Entrenador(entrenador['nombre'],
                                     entrenador['torneos_ganados'],
                                     entrenador['batallas_perdidas'],
                                     entrenador['batallas_ganadas']), 'nombre')
lista_entrenadores.barrido()

for ent in dic_entrenadores:
     for i in range(randint(0, 4)):
        pokemon= choice(dic_pokemones)
        pos =lista_entrenadores.busqueda(ent['nombre'],'nombre')
        pos.sublista.insertar(Pokemon(pokemon['nombre'],
                                     pokemon['nivel'],
                                     pokemon['tipo'],
                                     pokemon['subtipo']), 'nombre')



lista_entrenadores.barrido_lista_lista()
entrenador = input('ingrese nombre del entrenador ') #a
if(pos):
    print(f'el entrenador tiene {pos.sublista.tamanio()} pokemones')
else:
    print('el entrenador no tiene pokemones')
print('Entrenadores que tienen mas de 3 pokemones')

lista_entrenadores.barrido_entrenador_mas_tres()#B

mayor=lista_entrenadores.mayor_de_lista('torneos_ganados')#busqueda seciencial #C
if(mayor):
    Mayornivel = mayor.sublista.mayor_de_lista('nivel').info
    print(f'El entrenador con mas batallas ganadas es {mayor.info} y su pokemon de mayor nivel es {Mayornivel}')
else:
    print('No hay torneos ganados')

entrenador = input('ingrese nombre del entrenador ')#D
pos = lista_entrenadores.busqueda(entrenador,'nombre')
if(pos):
    print(f"entrenador {pos.info}")
    print('sus pokemons son')
    pos.sublista.barrido()
else:
    print('el entrenador no esta en la lista')

print('entrenadores con mas del 79% de victorias son')#E
lista_entrenadores.barrido_porcentaje_victorias()

print('Los entrenadores que tienen pokemones de tipo fuego o planta, o subtipo volador o agua son:')#F
lista_entrenadores.barrido_tipo_subtipo()

entrenador = input('ingrese nombre del entrenador ')#G
pos=lista_entrenadores.busqueda(entrenador,'nombre')
print('el promedio del nievel de los pokemones del entrenador ', entrenador, ' es')
print(lista_entrenadores.promedio_de_nivel_pekemones(pos))

pokemon = input('ingrese nombre del pokemon ')#H
print('A ', pokemon, ' lo tienen esta cantidad de entrenadores')
print(lista_entrenadores.barrido_cantidad_de_pokemones_repetidos('pokemon'))

print('Los entrenadores que tienen pokemones repetidos son ')#I
lista_entrenadores.barrido_entrenador_con_pokemon_repetidos()

print('los entrenadores que tienen pokemon Wingull, yrantrum o Terrakion son')#J
lista_entrenadores.barrido_pokemon_Tyrantrum_Terrakion_Wingull()

entrenador = input('ingrese nombre del entrenador ')#K
pos=lista_entrenadores.busqueda(entrenador,'nombre')
if(pos):
    print(f"entrenador {pos.info}")
    pokemon = input('ingrese nombre del pokemon ')
    posicion= pos.sublista.busqueda(pokemon, 'nombre')
    if(posicion):
        print(f"pokemon {posicion.info}")
else:
    print('el entrenador no esta en la lista')