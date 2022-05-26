#Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, 
# el nombre del superhéroe y su género (Masculino M y Femenino 
#F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F},
#  etc., desarrollar un algoritmo que resuelva las siguientes actividades:
#a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
#b. mostrar los nombre de los superhéroes femeninos;
#c. mostrar los nombres de los personajes masculinos;
#d. determinar el nombre del superhéroe del personaje Scott Lang;
#e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
#con la letra S;
#f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
#de superhéroes.
from cola import Cola
cola1=Cola()
class Pelicula():
    nombre, nombre_superheroe, genero = None, None, None
   
nombre= ['Scott Lang','Steve Rogers', 'Peter Parker','Natasha Romanoff', 'Wanda Maximoff',' Stephen Strange','Carol Danvers']
nombre_superheroe=['Ant-Man','Capitán América', 'Spder Man','Black Widor', 'La bruja escarlata','Dr Strange','Capitana Marvel']
genero= ['M','M','M','F','F','M','F']


for i in range(len(nombre)):
    dato = Pelicula()
    dato.nombre= nombre[i]
    dato.nombre_superheroe= nombre_superheroe[i]
    dato.genero=genero[i]
    dic ={'nombre': nombre[i], 'nombre del superheroe': nombre_superheroe[i], 'genero':genero[i]}
    print(dato.nombre, dato.nombre_superheroe, dato.genero)
    cola1.arribo(dato)
femenino =[]
masculino=[]
nom_scottLang=''
nom_carolDanvers=''
class Nombre_s():
    nombre,nombre_superheroe,genero = None,None,None
    def __init__(self, nombre, nombre_superheroe, genero):
        self.nombre=nombre
        self.nombre_superheroe=nombre_superheroe
        self.genero=genero
    
    def __str__(self):
        return f' {self.nombre} {self.nombre_superheroe} {self.genero} '
nombre_conS=[]
while (not cola1.cola_vacia()):
    dato= cola1.atencion()
    if(dato.nombre_superheroe == 'Capitana Marvel'):
        print('nombre de la capitana marvel es', dato.nombre)
    if (dato.genero == 'F'):
        femenino.append(dato.nombre)
    if(dato.genero == 'M'):
        masculino.append(dato.nombre)
    if(dato.nombre == 'Scott Lang'):
        nom_scottLang=dato.nombre_superheroe
    if (dato.nombre[0] == 'S'):
            nombre_conS.append(Nombre_s(dato.nombre, dato.nombre_superheroe, dato.genero))
            
    if(dato.nombre == 'Carol Danvers'):
        nom_carolDanvers=dato.nombre_superheroe
       
print('los personajes femeninos son:')
for i in range(len(femenino)):
    print(femenino[i])
print('los personajes masculinos son')
for i in range(len(masculino)):
    print(masculino[i])
print('nombre del superheroe de scott Lang es:', nom_scottLang)
print('los personajes cuyos nombre comienzan con S son')
for i in range(len(nombre_conS)):
    print(nombre_conS[i])
print('nombre de superheroe de Carol Danvers es ', nom_carolDanvers)
