from cola import Cola
from heap import HeapMin, HeapMax


def criterio(dato, campo=None):
    dic = {}
    if (hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if (campo is None or campo not in dic):
        return dato
    else:
        return dic[campo]


class nodoArista():
    info, sig, peso, datos = None, None, None, None
    # ? info es el destino


class nodoVertice():
    info, sig, visitado, adyacentes, datos = None, None, False, None, None


class Arista():

    def __init__(self):
        self.__inicio = None
        self.__tamanio = 0

    def get_inicio(self):
        return self.__inicio

    def insertar_arista(self, dato, peso, datos=None, campo=None):
        nodo = nodoArista()
        nodo.info = dato
        nodo.peso = peso
        nodo.datos = datos

        if (self.__inicio is None or criterio(nodo.info, campo) < criterio(self.__inicio.info, campo)):
            nodo.sig = self.__inicio
            self.__inicio = nodo
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while (actual is not None and criterio(nodo.info, campo) > criterio(actual.info, campo)):
                anterior = anterior.sig
                actual = actual.sig

            nodo.sig = actual
            anterior.sig = nodo

        self.__tamanio += 1

    def tamanio(self):
        return self.__tamanio

    def barrido_aristas(self):
        aux = self.__inicio
        while (aux is not None):
            print(aux.info, aux.peso)
            aux = aux.sig

    def busqueda_arista(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while (aux is not None and pos is None):
            if (criterio(aux.info, campo) == buscado):
                pos = aux
            aux = aux.sig

        return pos

    def busqueda_arista_datos(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while (aux is not None and pos is None):
            if (criterio(aux.datos)[campo] == buscado):
                pos = aux
            aux = aux.sig

        return pos

    def eliminar_arista(self, clave, campo=None):
        dato, peso = None, None
        if self.__inicio is not None:
            if (criterio(self.__inicio.info, campo) == clave):
                dato = self.__inicio.info
                peso = self.__inicio.peso
                self.__inicio = self.__inicio.sig
            else:
                anterior = self.__inicio
                actual = self.__inicio.sig
                while (actual is not None and criterio(actual.info, campo) != clave):
                    anterior = anterior.sig
                    actual = actual.sig

                if (actual is not None):
                    dato = actual.info
                    peso = actual.peso
                    anterior.sig = actual.sig
            if dato:
                self.__tamanio -= 1

        return dato, peso

    def obtener_elemento_arista(self, indice):
        if (indice <= self.__tamanio-1 and indice >= 0):
            aux = self.__inicio
            for i in range(indice):
                aux = aux.sig
            return aux.info
        else:
            return None


class Grafo():

    def __init__(self, dirigido=True):
        self.__inicio = None
        self.__tamanio = 0
        self.__dirigido = dirigido

    def insertar_vertice(self, dato, datos=None, campo=None):
        nodo = nodoVertice()
        nodo.info = dato
        nodo.adyacentes = Arista()
        nodo.datos = datos

        if (self.__inicio is None or criterio(nodo.info, campo) < criterio(self.__inicio.info, campo)):
            nodo.sig = self.__inicio
            self.__inicio = nodo
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while (actual is not None and criterio(nodo.info, campo) > criterio(actual.info, campo)):
                anterior = anterior.sig
                actual = actual.sig

            nodo.sig = actual
            anterior.sig = nodo

        self.__tamanio += 1

    def insertar_arista(self, origen, destino, peso, datos=None):
        vert_origen = self.busqueda_vertice(origen)
        vert_destino = self.busqueda_vertice(destino)
        if (vert_origen and vert_destino):
            vert_origen.adyacentes.insertar_arista(destino, peso, datos)
            if not self.__dirigido:
                vert_destino.adyacentes.insertar_arista(origen, peso, datos)

    def tamanio(self):
        return self.__tamanio

    def barrido_vertice(self):
        aux = self.__inicio
        while (aux is not None):
            print(aux.info)
            aux = aux.sig

    def marcar_no_visitado(self):
        aux = self.__inicio
        while (aux is not None):
            aux.visitado = False
            aux = aux.sig

    def barrido_lista_lista(self):
        aux = self.__inicio
        while (aux is not None):
            print('Vertice:', aux.info)
            print('arsitas:')
            aux.adyacentes.barrido_aristas()
            aux = aux.sig

    def busqueda_vertice(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while (aux is not None and pos is None):
            if (criterio(aux.info, campo) == buscado):
                pos = aux
            aux = aux.sig

        return pos

    def barrido_no_visitado(self):
        aux = self.__inicio
        while (aux is not None):
            if not aux.visitado:
                print(aux.info)
            aux = aux.sig

    def eliminar_vertice(self, clave, campo=None):
        dato = None
        if self.__inicio is not None:
            if (criterio(self.__inicio.info, campo) == clave):
                dato = self.__inicio.info
                self.__inicio = self.__inicio.sig
            else:
                anterior = self.__inicio
                actual = self.__inicio.sig
                while (actual is not None and criterio(actual.info, campo) != clave):
                    anterior = anterior.sig
                    actual = actual.sig

                if (actual is not None):
                    dato = actual.info
                    anterior.sig = actual.sig
            if dato:
                self.__tamanio -= 1

            #! eliminar todas las aristas que apuntan al vertice
            aux = self.__inicio
            while (aux is not None):
                aux.adyacentes.eliminar_arista(clave)
                aux = aux.sig

        return dato

    def eliminar_arista(self, origen, destino):
        vert_origen = self.busqueda_vertice(origen)
        valor, peso = None, None
        if vert_origen:
            valor, peso = vert_origen.adyacentes.eliminar_arista(destino)
            if valor:
                vert_destino = self.busqueda_vertice(destino)
                vert_destino.adyacentes.eliminar_arista(origen)

        return peso

    def obtener_elemento_vertice(self, indice):
        if (indice <= self.__tamanio-1 and indice >= 0):
            aux = self.__inicio
            for i in range(indice):
                aux = aux.sig
            return aux.info
        else:
            return None

    def es_adyacente(self, origen, destino):
        resultado = False
        vert_origen = self.busqueda_vertice(origen)
        if vert_origen:
            aux = vert_origen.adyacentes.busqueda_arista(destino)
            if aux:
                resultado = True
        return resultado

    def tareas_miembros(self, miembro):
        tareas = []
        aux = self.__inicio.adyacentes
        pos = self.__inicio.adyacentes.busqueda_arista_datos(
            miembro, 'Asignado a')
        if pos is not None:
            resultados = pos
            actividad = resultados.info
            print(actividad)
            tareas.append(actividad)
        aux = aux.sig

        return tareas

    def adyacentes(self, origen):
        vert_origen = self.busqueda_vertice(origen)
        if vert_origen:
            vert_origen.adyacentes.barrido_aristas()

    def existe_paso(self, origen, destino):
        resultado = False
        vert_origen = self.busqueda_vertice(origen)
        if not vert_origen.visitado:
            vert_origen.visitado = True
            print(vert_origen.info)
            adyacentes = vert_origen.adyacentes.get_inicio()
            # resultado = g.es_adyacente(origen, destino)
            while adyacentes is not None and not resultado:
                if adyacentes.info == destino:
                    resultado = True
                else:
                    resultado = self.existe_paso(adyacentes.info, destino)
                adyacentes = adyacentes.sig
        return resultado

    def barrido_profundidad(self, origen):
        vert_origen = self.busqueda_vertice(origen)
        if not vert_origen.visitado:
            print(vert_origen.info)
            vert_origen.visitado = True
            adyacentes = vert_origen.adyacentes.get_inicio()
            while adyacentes is not None:
                self.barrido_profundidad(adyacentes.info)
                adyacentes = adyacentes.sig

    def barrido_profundidad_star(self, origen, grafo):
        vert_origen = self.busqueda_vertice(origen)
        if not vert_origen.visitado:
            grafo.insertar_vertice(vert_origen)
            vert_origen.visitado = True
            adyacentes = vert_origen.adyacentes.get_inicio()
            while adyacentes is not None:
                self.barrido_profundidad_star(adyacentes.info, grafo)
                adyacentes = adyacentes.sig

    def barrido_amplitud(self, origen):
        self.marcar_no_visitado()
        vert_origen = self.busqueda_vertice(origen)
        pendientes = Cola()
        if not vert_origen.visitado:
            vert_origen.visitado = True
            pendientes.arribo(vert_origen)
            while not pendientes.cola_vacia():
                vertice_actual = pendientes.atencion()
                print(vertice_actual.info)
                adyacentes = vertice_actual.adyacentes.get_inicio()
                while adyacentes is not None:
                    adyacente = self.busqueda_vertice(adyacentes.info)
                    if not adyacente.visitado:
                        adyacente.visitado = True
                        pendientes.arribo(adyacente)
                    adyacentes = adyacentes.sig

    def dijkstra(self, origen):
        from math import inf
        # self.marcar_no_visitado()
        no_visitado = HeapMin()
        camino = {}

        aux = self.__inicio
        while aux is not None:
            if aux.info == origen:
                no_visitado.agregar([aux, None], 0)
            else:
                no_visitado.agregar([aux, None], inf)
            aux = aux.sig

        while no_visitado.tamanio > 0:
            elemento, peso, _ = no_visitado.quitar()
            vertice, previo = elemento[0], elemento[1]
            camino[vertice.info] = {'previo': previo, 'peso': peso}
            adyacentes = vertice.adyacentes.get_inicio()
            while adyacentes is not None:
                buscado = no_visitado.buscar(adyacentes.info)
                if buscado:
                    if no_visitado.vector[buscado][1] > peso + adyacentes.peso:
                        no_visitado.vector[buscado][1] = peso + adyacentes.peso
                        no_visitado.vector[buscado][0][1] = vertice.info
                        no_visitado.flotar(buscado)
                adyacentes = adyacentes.sig
        return camino

    def kruskal(self):
        def buscar_en_bosque(bosque, buscado):
            for arbol in bosque:
                if buscado in arbol:
                    return arbol

        bosque = []
        aristas = HeapMin()
        aux = self.__inicio
        while aux is not None:
            print(aux)
            bosque.append(str(aux.info))
            adyacentes = aux.adyacentes.get_inicio()
            while adyacentes is not None:
                aristas.arribo([aux.info, adyacentes.info],
                               adyacentes.peso, adyacentes.datos)
                adyacentes = adyacentes.sig
            aux = aux.sig

        while len(bosque) > 1 and aristas.tamanio > 0:
            arista, peso, datos = aristas.quitar()
            # print(datos)
            # print(arista[0])
            # print(arista[1])
            origen = buscar_en_bosque(bosque, arista[0])
            destino = buscar_en_bosque(bosque, arista[1])
            # print(origen, destino, 'posiciones')
            if origen is not None and destino is not None:
                if origen != destino:
                    # print(arista[0], origen)
                    # print(arista[1], destino)
                    bosque.remove(origen)
                    bosque.remove(destino)
                    if ';' not in origen and ';' not in destino:
                        bosque.append(f'{origen};{destino};{peso};{datos}')
                    elif ';' in origen and ';' not in destino:
                        bosque.append(
                            origen+f'-{arista[0]};{destino};{peso};{datos}')
                    elif ';' not in origen and ';' in destino:
                        bosque.append(
                            destino+f'-{origen};{arista[1]};{peso};{datos}')
                    else:
                        bosque.append(origen+'-'+destino +
                                      f'-{arista[0]};{arista[1]};{peso};{datos}')

            # print(bosque)
            # a = input()
        return bosque

    def camino(self, resultados, origen, destino):
        camino_mas_corto = {'camino': [],
                            'costo': None}
        if destino in resultados:
            vert_destino = resultados[destino]
            camino_mas_corto['costo'] = vert_destino['peso']
            camino_mas_corto['camino'].append(destino)
            while vert_destino['previo'] is not None:
                camino_mas_corto['camino'].append(vert_destino['previo'])
                vert_destino = resultados[vert_destino['previo']]
            camino_mas_corto['camino'].reverse()
        return camino_mas_corto

    def contar_maravillas(self):
        paises = {}
        aux = self.__inicio
        while aux is not None:
            if aux.info not in paises:
                paises[aux.datos['pais']] = {'arq': False, 'naturales': False}
            if aux.datos['tipo'] == 'naturales':
                paises[aux.datos['pais']]['naturales'] = True
            else:
                paises[aux.datos['pais']]['arq'] == True
            aux = aux.sig
        return paises

    def episodios_star_wars(self):
        personajes = {}
        aux = self.__inicio
        while aux is not None:
            if aux.info not in personajes:
                if aux.adyacentes._Arista__inicio.peso > 2:
                    personajes['personaje 1'] = aux.info
                    personajes['personaje 2'] = aux.adyacentes._Arista__inicio.info
            aux = aux.sig
        return personajes

    def maravillas_arquitec_naturales(self):
        paises = {}
        paiss = {}
        aux = self.__inicio
        while aux is not None:
            paiss = aux.datos['pais'].split('-')
            for pais in paiss:
                if pais not in paises:
                    paises[pais] = {'arq': False, 'naturales': False}
                if aux.datos['tipo'] == 'naturales':
                    paises[pais]['naturales'] = True
                else:
                    paises[pais]['arq'] = True
            aux = aux.sig
        return paises

    def paises_mas_marivallas(self):
        paises = {}
        paiss = {}
        aux = self.__inicio
        while aux is not None:
            paiss = aux.datos['pais'].split('-')
            for pais in paiss:
                if pais not in paises:
                    paises[pais] = {'arquitectonica': 0, 'naturales': 0}
                    if aux.datos['tipo'] == 'naturales':
                        paises[pais]['naturales'] = 1
                    else:
                        paises[pais]['arquitectonica'] = 1
                elif pais in paises:
                    if paises[pais][aux.datos['tipo']]:
                        cantPais = paises[pais][aux.datos['tipo']] + 1
                        paises[pais][aux.datos['tipo']] = cantPais
                    else:
                        paises[pais][aux.datos['tipo']] = 1
            aux = aux.sig
        return paises

    def personajes_mayor_episodios_compartidos(self):
        personajes = {}
        aux = self.__inicio
        while aux is not None:
            personaje = aux.adyacentes._Arista__inicio.info
            if personaje not in personajes:
                personajes[personaje] = {'episodios': 0}
            else:
                cantEps = personajes[personaje]['episodios'] + 1
                personajes[personaje]['episodios'] = cantEps

            aux = aux.sig
        return personajes

#! algoritmos especiales dijkstra prim kruskal


g = Grafo(dirigido=False)

# g.insertar_vertice('T')
# g.insertar_vertice('Z')
# g.insertar_vertice('F')
# g.insertar_vertice('X')
# g.insertar_vertice('R')
# g.insertar_vertice('K')
# g.insertar_vertice('U')


#g.insertar_arista('T', 'X', 6)
#g.insertar_arista('T', 'F', 3)
#g.insertar_arista('T', 'R', 8)
#g.insertar_arista('F', 'X', 2)
#g.insertar_arista('F', 'R', 2)
#g.insertar_arista('X', 'Z', 9)
#g.insertar_arista('R', 'Z', 4)
#g.insertar_arista('K', 'Z', 3)
#g.insertar_arista('R', 'X', 5)
# g.insertar_arista('K', 'A', 31)
# g.insertar_arista('J', 'F', 31)
# g.insertar_arista('A', 'J', 0)

#arbol_min = g.kruskal()

#arbol_min = arbol_min[0].split('-')
#peso_total = 0
# for nodo in arbol_min:
#    nodo = nodo.split(';')
#    peso_total += int(nodo[2])
#    print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')

#print(f"el peso total es {peso_total}")

# if g.existe_paso('T', 'Z'):
#    resultados1 = g.dijkstra('T')
#    camino = g.camino(resultados1, 'T', 'Z')
#    print(camino)
# else:
#    print('no se puede llega de T a Z')
# g.eliminar_arista('A', 'C')
# g.eliminar_vertice('C')

# g.barrido_profundidad('K')
# print()
# g.barrido_amplitud('K')
# print()
# g.barrido_no_visitado()

# g.adyacentes('A')

# print(g.es_adyacente('A', 'F'))
# print(g.es_adyacente('Z', 'A'))
