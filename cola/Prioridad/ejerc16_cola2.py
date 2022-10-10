from heap import HeapMax
colaImpresion=HeapMax()

colaImpresion.agregar('doc empelado1', 1)
colaImpresion.agregar('doc empelado2', 1)
colaImpresion.agregar('doc empelado3', 1)
print(colaImpresion.vector)
print('Primer elemento de la cola:')#B
print(colaImpresion.vector[0][0])
colaImpresion.agregar('doc staff 1', 2)#C
colaImpresion.agregar('doc staff 2', 2)
colaImpresion.agregar('doc gerente', 3)#D
print('Los dos primeros elementos de la cola')#E
print(colaImpresion.vector[0:2])
colaImpresion.agregar('doc empelado4', 1)#F
colaImpresion.agregar('doc empelado5', 1)
colaImpresion.agregar('doc gerente2', 3)
print('Cola de impresion')#G
print(colaImpresion.vector)