from lista_2 import Lista
from cola_copy import Cola
from jurassic_park import dinosaurs
file = open('alerts.txt')
lineas = file.readlines()



lineas.pop(0)  # quitar cabecera


class Dinosaurio():

    def __init__(self, name, type, number, period,named_by,anio):
        self.name = name
        self.type = type
        self.number = number
        self.period = period
        self.named_by = named_by
        self.anio=anio

    def __str__(self):
        return f'{self.name}-{self.type}-{self.number}-{self.period}-{self.named_by}-{self.anio}'
class Dino():

    def __init__(self, time, zone_code, dino_number, alert_level):
        self.time = time
        self.zone_code = zone_code
        self.dino_number = dino_number
        self.alert_level = alert_level
        

    def __str__(self):
        return f"{self.time} | {self.zone_code} | {self.dino_number} | {self.alert_level}"
lista_dinosaurio= Lista()
lista_claire=Lista()
for dino in dinosaurs:
    lista_dinosaurio.insertar(Dinosaurio(dino['name'],
                                        dino['type'],
                                        dino['number'],
                                        dino['period'],
                                        dino['named_by'],
                                        dino['named_by'][len(dino['named_by'])-4:]),'name')
lista_dinosaurio.barrido()
print('ultimo dinosaurio descubierto y quien lo hizo')
print(lista_dinosaurio.barrido_ultimo_dinosaurio().info)
for dato in lineas:   
    datos = dato.split(';')   
    pos =lista_dinosaurio.busqueda(int(datos[2]),'number')
    pos.sublista.insertar(Dino(datos[0],
                                datos[1],
                                datos[2],
                                datos[3]),'time')

lista_dinosaurio.barrido_lista_lista()
for dino in dinosaurs:
    lista_claire.insertar(Dinosaurio(dino['name'],
                                        dino['type'],
                                        dino['number'],
                                        dino['period'],
                                        dino['named_by'],
                                        dino['named_by'][len(dino['named_by'])-4:]),'anio')
for dato in lineas:   
    datos = dato.split(';')   
    pos =lista_claire.busqueda(int(datos[2]),'number')
    pos.sublista.insertar(Dino(datos[0],
                                datos[1],
                                datos[2],
                                datos[3]),'time')
lista_claire.barrido_lista_lista()
print('Eliminando infomracion de zonas de ambas listas')
lista_dinosaurio.barrido_eliminacion_zona()
lista_claire.barrido_eliminacion_zona()
lista_dinosaurio.barrido_lista_lista()


print('modificar el registro de Mosasaurus')
datos = lista_dinosaurio.barrido_modificar_registro()
print(datos)
dato_eliminado=datos.eliminar(datos.info.name,'name')
if(dato_eliminado):
    lista_dinosaurio.insertar(Dinosaurio('Mosasaurus',dato_eliminado.type,dato_eliminado.number,dato_eliminado.period,dato_eliminado.named_by,dato_eliminado.anio),'name')
    pos=lista_dinosaurio.busqueda('Mosasaurus','name')
    pos.sublista=dato_eliminado.sublista
print('Barrido filtrado por nombre y nivel')

lista_dinosaurio.barrido_nombre_nivel()
carnivoros,herbivoros=lista_dinosaurio.barrido_carnivoro_herbivoro()

cola_carnivoros=Cola()
cola_herbivoros=Cola()
for i in carnivoros:
    cola_carnivoros.arribo(i)  
for i in herbivoros:
    cola_herbivoros.arribo(i)  
print('cola carnivoro')
while (not cola_carnivoros.cola_vacia()):
    dato= cola_carnivoros.atencion()
    if('EPC944' != dato.zone_code):
        print(dato)
print('cola herviboro')
while (not cola_herbivoros.cola_vacia()):
    dato= cola_herbivoros.atencion()
    if('EPC944' != dato.zone_code):
        print(dato)
print('dinosaurios Raptors y Carnotaurus ')
lista_dinosaurio.barrido_algunos_dino()
print('codigo de zona de dinosaurios Compsognathus')
lista_dinosaurio.barrido_codigos_Compsognathus()

def mosquito(clave):
    if(clave > 33) and (clave < 47):
        return 'mosquito'
    elif (clave % 3 == 0):
        return  mosquito((clave//2)+9)
    else:
        return   mosquito(clave - 14) 
print(mosquito(456))