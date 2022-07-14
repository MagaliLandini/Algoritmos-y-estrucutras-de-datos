#Se cuenta con una lista de películas de cada una de estas se dispone de los siguientes datos: 
#nombre, valoración del público –es un valor comprendido entre 0-10–, año de estreno y recaudación.
#  Desarrolle los algoritmos necesarios para realizar las siguientes tareas:
#a. permitir filtrar las películas por año –es decir mostrar todas las películas de un determinado año–;
#[118]
#b. mostrar los datos de la película que más recaudo;
#c. indicar las películas con mayor valoración del público, puede ser más de una;
#d. mostrar el contenido de la lista en los siguientes criterios de orden –solo podrá utilizar una 
#lista auxiliar–:
#I. por nombre,
#II. por recaudación,
#III. por año de estreno,
#IV. por valoración del público
from lista_2 import Lista
lista_peliculas = Lista()
lista_aux= Lista()

class Peliculas():

    def __init__(self, nombre, valoracion, anio_estreno, recaudacion):
        self.nombre = nombre
        self.valoracion = valoracion
        self.anio_estreno = anio_estreno
        self.recaudacion = recaudacion

    def __str__(self):
        return f'{self.nombre}-{self.valoracion}-{self.anio_estreno}-{self.recaudacion}'
dic_peliculas = [
    {'nombre': 'Titanic', 'valoracion': 3, 'anio_estreno': 1990, 'recaudacion': 10.000},
    {'nombre': 'los vengadores', 'valoracion': 1, 'anio_estreno': 2011, 'recaudacion': 3.000},
    {'nombre': 'esperando a la carroza', 'valoracion': 3, 'anio_estreno': 1980, 'recaudacion': 1.000},
    {'nombre': 'interceptado', 'valoracion': 0, 'anio_estreno': 2022, 'recaudacion': 500.000},
    {'nombre': 'los minions', 'valoracion': 2, 'anio_estreno': 2015, 'recaudacion': 4.000}]

for pelicula in dic_peliculas:
    print(pelicula)
    lista_peliculas.insertar(Peliculas(pelicula['nombre'],
                                        pelicula['valoracion'],
                                        pelicula['anio_estreno'],
                                        pelicula['recaudacion']),'nombre')
print(lista_peliculas.barrido())

anio=int(input('ingrese el año que desea buscar '))#A
lista_peliculas.barrido_anio_estreno(anio) 

print('pelicula con mas recaudacion')#B
print(lista_peliculas.barrido_pelicula_mas_recaudo().info)

print('pelicula mas valorada')#C
valorada=lista_peliculas.barrido_pelicula_mas_valorada()
valorada.barrido()

var=input('ingrese el campo por el cual desea ordenar (nombre,valoracion,anio_estreno,recaudacion) ')#D En este caso al hacer el barrido me devuelve none al final de la lista, no se en que estoy fallando.
for pelicula in dic_peliculas:
    lista_aux.insertar(Peliculas(pelicula['nombre'],
                                        pelicula['valoracion'],
                                        pelicula['anio_estreno'],
                                        pelicula['recaudacion']), var )
print(lista_aux.barrido())