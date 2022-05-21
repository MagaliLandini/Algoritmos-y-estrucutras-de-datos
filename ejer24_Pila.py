# Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de 
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones 
#necesarias para resolver las siguientes actividades:
#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
#b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
from msilib.schema import Class
from pila import Pila
pila1 = Pila()

class Personaje():
    nombre,cantPeliculas = None,None
nombre = ['thor','Iron Man','Hulk','Dr Strange','Loki','Rocket Raccoon','Groot', 'Black Widow']
cantPeliculas = [5,6,4,3,3,1,2,4]

for i in range(len(nombre)):
    dato = Personaje()
    dato.nombre = nombre[i]
    dato.cantPeliculas = cantPeliculas[i]
    dic = {'nombre': nombre[i], 'Cantidad de peliculas': cantPeliculas[i]}
    print(dato.nombre, dato.cantPeliculas)
    pila1.apilar(dato)

PosRaccoon=1
posGroot=1
rocketEncontrado= False
grootEncontrado= False
PersQuePartSaga=[]
PelicViaudaNegra=0
Letras= ['C','D','G']
personajesLetras= []


while (not pila1.pila_vacia()):
    dato= pila1.desapilar()
    
    if (dato.nombre != "Rocket Raccoon" and rocketEncontrado is False):
        PosRaccoon = PosRaccoon + 1
    elif (dato.nombre == 'Rocket Raccoon'):
        rocketEncontrado= True
    if (dato.nombre != 'Groot' and grootEncontrado is False):
        posGroot += 1
    elif(dato.nombre == 'Groot'):
        grootEncontrado = True
    if (dato.cantPeliculas >= 5):
        PersQuePartSaga.append(dato)
    if (dato.nombre == 'Black Widow'):
        PelicViaudaNegra = dato.cantPeliculas
    if (dato.nombre[0] in Letras):
        personajesLetras.append(dato)




print('Rocket Raccoon se encuentra en la posicion: ', PosRaccoon)
print ('Groot se encuentra en la posicion: ', posGroot)
print('Personajes que participaron en mas de 5 peliculas de la saga y cantidad de peliculas que realizaron')
for i in range(len(PersQuePartSaga)):
    print(PersQuePartSaga[i].nombre,PersQuePartSaga[i].cantPeliculas)

print('cantidad de peliculas en la que participo la viuda negra: ', PelicViaudaNegra)
print('Personajes que comienzan con C,D,G: ')
for i in range(len(personajesLetras)):
    print(personajesLetras[i].nombre)