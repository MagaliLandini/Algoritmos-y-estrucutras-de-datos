# Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de
#  estreno, desarrollar las funciones necesarias para resolver las siguientes actividades:
#a. mostrar los nombre películas estrenadas en el año 2014;
#[85]
#b. indicar cuántas películas se estrenaron en el año 2018;
#c. mostrar las películas de Marvel Studios estrenadas en el año 2016.

from pila import Pila
pila1=Pila()

class Pelicula():
    titulo, estudio_cinematografico, anio = None, None, None
titulo=['iron man','Thor', 'Spder Man','Batman', 'La mujer Maravilla','El wason']
estudio_cinematografico=['Marvel Studio','Marvel Studio' ,'Sony', 'DC Studio', 'Marvel Studios', 'DC studio']
anio= [2014,2016,2018,2014,2016,2010]

for i in range(len(titulo)):
    dato = Pelicula()
    dato.titulo = titulo[i]
    dato.estudio_cinematografico = estudio_cinematografico[i]
    dato.anio = anio[i]
    dic = {'titulo': titulo[i], 'estudio cinematografico': estudio_cinematografico[i], 'año': anio[i]}
    print(dato.titulo, dato.estudio_cinematografico, dato.anio)
    pila1.apilar(dato)
con=0
peliculasMarvel= []
print('las peliculas estrenadas en 2014 son: ')
while(not pila1.pila_vacia()):
    dato=pila1.desapilar()
    if(dato.anio == 2014):
        print(dato.titulo)
    if (dato.anio == 2018):
        con = con + 1
    if (dato.anio == 2016 and dato.estudio_cinematografico == "Marvel Studios"):
        peliculasMarvel.append(dato.titulo)
        

print('en 2018 se estrenaron ', con , 'peliculas')
print('Peliculas de Marvel Studios estrenadas en 2016: ')
for i in range(len(peliculasMarvel)):
    print(peliculasMarvel[i])

