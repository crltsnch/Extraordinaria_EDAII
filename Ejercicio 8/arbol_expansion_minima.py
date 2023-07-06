from grafo_planetas import *
from nodos import NodoArista, NodoVertice, Grafo, Arista

def buscar_vertice(grafo, buscado):
    aux = grafo.inicio
    while aux is not None and aux.info != buscado:
        aux = aux.sig
    return aux

def obtener_arbol_expansion_minima(grafo):
    bosque = [[grafo.inicio.info]]
    aristas = []
    adyacentes = grafo.inicio.adyacentes.info
    while adyacentes is not None:
        aristas.append([grafo.inicio.info, adyacentes.destino, adyacentes.info])
        adyacentes = adyacentes.sig
    
    while (len(bosque[0])//2) < grafo.tamanio-1:
        menor = inf
        menor_arista = None
        tipo = None
        for arista in aristas:
            origen = arista[0]
            destino = arista[1]

            if origen not in bosque[0] and destino in bosque[0]:
                if arista[2] < menor:
                    menor, menor_arista = arista[2], arista
                    tipo = True
            
            if origen in bosque[0] and destino not in bosque[0]:
                if arista[2] < menor:
                    menor, menor_arista = arista[2], arista
                    tipo = False
            
    arista = aristas.pop(aristas.index(menor_arista))
    if len(bosque[0]) != 1:
        bosque[0] += [arista[0], arista[1]]
    else:
        bosque.pop()
        bosque.append([arista[0], arista[1]])

    aux = None
    if tipo:
        aux = buscar_vertice(grafo, arista[0])
