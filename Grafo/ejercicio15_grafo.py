from grafo import Grafo
g = Grafo(dirigido=False)


g.insertar_vertice('Bahía de Ha Long',datos={'tipo':'naturales','pais':'Vietnam'})
g.insertar_vertice('Amazonia',datos={'tipo':'naturales','pais':'Bolivia-Brasil-Colombia-Ecuador-Guayana Francesa-Guayana-Perú-Suriman-Venezuela'})
g.insertar_vertice('Montaña de la Mesa',datos={'tipo':'naturales','pais':'Sudáfrica'})
g.insertar_vertice('Cataratas del Iguazú',datos={'tipo':'naturales','pais':'Argentina-Brasil-Paraguay'})
g.insertar_vertice('Isla Jeju',datos={'tipo':'naturales','pais':'Corea del Sur'})
g.insertar_vertice('Parque Nacional de Komodo',datos={'tipo':'naturales','pais':'Indonesia'})
g.insertar_vertice('Parque Nacional del río subterráneo de Puerto Princesa',datos={'tipo':'naturales','pais':'Filipinas'})
g.insertar_vertice('Palacio Legislativo',datos={'tipo':'arquitectonica','pais':'Rumania'})
g.insertar_vertice('Gran Mezquita de Djenné',datos={'tipo':'arquitectonica','pais':'Mali'})
g.insertar_vertice('Fuerte Derawar',datos={'tipo':'arquitectonica','pais':'Parkistán'})
g.insertar_vertice('Chand Baori',datos={'tipo':'arquitectonica','pais':'India'})
g.insertar_vertice('Puente de Mostar',datos={'tipo':'arquitectonica','pais':'Bosnia y Herzegovina'})
g.insertar_vertice('Gran Muralla',datos={'tipo':'arquitectonica','pais':'India'})
g.insertar_vertice('Mezquita de Sheikh Lotfollauiteh',datos={'tipo':'arquitectonica','pais':'Irán'})

g.insertar_arista('Bahía de Ha Long','Amazonia',4)
g.insertar_arista('Bahía de Ha Long','Montaña de la Mesa',5)
g.insertar_arista('Bahía de Ha Long','Cataratas del Iguazú',43)
g.insertar_arista('Bahía de Ha Long','Isla Jeju',3)
g.insertar_arista('Bahía de Ha Long','Parque Nacional de Komodo',2)
g.insertar_arista('Bahía de Ha Long','Parque Nacional del río subterráneo de Puerto Princesa',9)
g.insertar_arista('Amazonia','Montaña de la Mesa',43)
g.insertar_arista('Amazonia','Cataratas del Iguazú',77)
g.insertar_arista('Amazonia','Isla Jeju',87)
g.insertar_arista('Amazonia','Parque Nacional de Komodo',54)
g.insertar_arista('Amazonia','Parque Nacional del río subterráneo de Puerto Princesa',4)
g.insertar_arista('Montaña de la Mesa','Cataratas del Iguazú',4)
g.insertar_arista('Montaña de la Mesa','Isla Jeju',4)
g.insertar_arista('Montaña de la Mesa','Parque Nacional de Komodo',4)
g.insertar_arista('Montaña de la Mesa','Parque Nacional del río subterráneo de Puerto Princesa',4)
g.insertar_arista('Cataratas del Iguazú','Isla Jeju',4)
g.insertar_arista('Cataratas del Iguazú','Parque Nacional de Komodo',4)
g.insertar_arista('Cataratas del Iguazú','Parque Nacional del río subterráneo de Puerto Princesa',4)
g.insertar_arista('Isla Jeju','Parque Nacional de Komodo',4)
g.insertar_arista('Isla Jeju','Parque Nacional del río subterráneo de Puerto Princesa',4)
g.insertar_arista('Parque Nacional de Komodo','Parque Nacional del río subterráneo de Puerto Princesa',4)
g.insertar_arista('Palacio Legislativo','Gran Mezquita de Djenné',8)
g.insertar_arista('Palacio Legislativo','Fuerte Derawar',4)
g.insertar_arista('Palacio Legislativo','Chand Baori',9)
g.insertar_arista('Palacio Legislativo','Puente de Mostar',4)
g.insertar_arista('Palacio Legislativo','Gran Muralla',20)
g.insertar_arista('Palacio Legislativo','Mezquita de Sheikh Lotfollauiteh',4)
g.insertar_arista('Gran Mezquita de Djenné','Fuerte Derawar',4)
g.insertar_arista('Gran Mezquita de Djenné','Chand Baori',4)
g.insertar_arista('Gran Mezquita de Djenné','Puente de Mostar',32)
g.insertar_arista('Gran Mezquita de Djenné','Gran Muralla',4)
g.insertar_arista('Gran Mezquita de Djenné','Mezquita de Sheikh Lotfollauiteh',4)
g.insertar_arista('Fuerte Derawar','Chand Baori',4)
g.insertar_arista('Fuerte Derawar','Puente de Mostar',12)
g.insertar_arista('Fuerte Derawar','Gran Muralla',4)
g.insertar_arista('Fuerte Derawar','Mezquita de Sheikh Lotfollauiteh',4)
g.insertar_arista('Chand Baori','Puente de Mostar',58)
g.insertar_arista('Chand Baori','Gran Muralla',22)
g.insertar_arista('Chand Baori','Mezquita de Sheikh Lotfollauiteh',4)
g.insertar_arista('Puente de Mostar','Gran Muralla',3)
g.insertar_arista('Puente de Mostar','Mezquita de Sheikh Lotfollauiteh',4)
g.insertar_arista('Gran Muralla','Mezquita de Sheikh Lotfollauiteh',11)



print('Arbol de expansion minima')
arbol_min=g.kruskal()
print(arbol_min)
naturales=0
arquitectonicas=0
for i in arbol_min:
    peso_total = 0
    arbol_split=i.split('-')
    for nodo in arbol_split:
        nodo = nodo.split(';')
        peso_total += int(nodo[2])
        print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')
    if(i == arbol_min[0]):
        naturales=peso_total
    else:
        arquitectonicas=peso_total
print()
print('la expasion minima de las naturales es: ', naturales)
print()
print('la expasion minima de las arquitectonicas es: ', arquitectonicas)
print()
print('Cantidad de maravillas de tipo naturales y arquitecnocias que tiene cada pais')
print()
paises=g.paises_mas_marivallas()
for pais in paises:    
    print(pais,paises[pais])
print()
print('El pais tiene maravillas arquitectonicas y/o naturales?')
print()
paises=g.maravillas_arquitec_naturales()
for pais in paises:
    print(pais,paises[pais])





