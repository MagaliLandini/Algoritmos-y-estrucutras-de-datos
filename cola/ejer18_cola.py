#dada una cola con los códigos de turnos de atención (con el formato #@@@, donde # es una 
#letra de la A hasta la F y “@@@” son tres dígitos desde el 000 al 999), desarrollar un algoritmo 
#que resuelva las siguientes situaciones:
#a. cargar 1000 turnos de manera aleatoria a la cola.
#b. separar la cola con datos en dos colas, cola_1 con los turnos que empiezan con la letra A, C
#y F, y la cola_2 con el resto de los turnos (B, D y E).
#c. determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál de las letras 
#tiene mayor cantidad.
#d. mostrar los turnos de la cola con menor cantidad de elementos, cuyo número de turno sea 
#mayor que 506
from cola import Cola
from random import randint
cola1=Cola()
cola_1=Cola()
cola_2=Cola()
MenorCola=[]

def random_character():
     return chr(randint(65, 70)) #! mayuscula


for i in range(5):
    dato = random_character() + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
    cola1.arribo(dato)

while(not cola1.cola_vacia()):
    dato=cola1.atencion()
    print(dato[0:4])
    if (dato[0] in ['A','C','F']):
        cola_1.arribo(dato)
    elif (dato[0] in ['B','D','E']):
        cola_2.arribo(dato)
a=0
c=0
f=0
b=0
d=0
e=0
if(cola_1.tamanio() < cola_2.tamanio()):
    print('Cola 2 tiene mayor tamaño')
    while (not cola_2.cola_vacia()):
        dato= cola_2.atencion()
        if(dato[0] in 'B'):
            b +=1
        elif(dato[0] in 'D'):
            d +=1
        else:
            e +=1
    if(b > d and b > e):
                print('la letra B tiene mayor cantidad')
    elif(d > b and d > e):
            print('la letra D tiene mayor cantidad')
    elif (e> b and e > d):
            print('la letra E tiene mayor cantidad')  
    while(not cola_1.cola_vacia()):
     dato2= cola_1.atencion()
     if(int(dato2[1:4]) > 506 ):
         MenorCola.append(dato2)
     print('la cola 2 tiene menos turnos, y los turnos mayores a 506 son: ')
else:
    print('Cola 1 tiene mayor tamaño')
    while (not cola_1.cola_vacia()):
        dato= cola_1.atencion()
        if(dato[0] in 'A'):
            a +=1
        elif(dato[0] in 'C'):
            c +=1
        else:
            f +=1
    if(a > c and a > f):
                print('la letra A tiene mayor cantidad')
    elif(c > a and c > f):
            print('la letra C tiene mayor cantidad')
    elif (f> a and f > c):
            print('la letra F tiene mayor cantidad')     
    while(not cola_2.cola_vacia()):
     dato2= cola_2.atencion()
     if(int(dato2[1:4]) > 506 ):
         MenorCola.append(dato2)
    print('la cola 2 tiene mnos turnos, y los turnos mayores a 506 son: ')

for i in range(len(MenorCola)):
    print(MenorCola[i])


