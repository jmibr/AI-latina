#primer problema de la tarea
grafica = {'A':{'B':5, 'C':9}, 'B':{'E':10, 'F':7}, 'C':{'E':5, 'D':3}, 'F':{'H':8}, 'E':{'D':1,'G':4, 'H':2}, 'D':{'E':1,'G':4}, 'H':{'I':6}, 'G':{'I':12}, 'I':{'H':6,'G':12}}
def dijkstra(grafica,inicio,meta):
    distanciamin = {} 
    path = {} 
    novisitados = grafica    
    n = 2424242424      
    caminof = []    

    for node in novisitados:
        distanciamin[node] = n
    distanciamin[inicio] = 0

    while novisitados:
        nodomindist = None

        for node in novisitados:
            if nodomindist is None:
                nodomindist = node
            elif distanciamin[node] < distanciamin[nodomindist]:
                nodomindist = node

        alternativas = grafica[nodomindist].items()

        for hijo, peso in alternativas:

            if peso + distanciamin[nodomindist] < distanciamin[hijo]:
                distanciamin[hijo] = peso + distanciamin[nodomindist]
                path[hijo] = nodomindist

        novisitados.pop(nodomindist)

    nodoactual = meta

    while nodoactual != inicio:
        try:
            caminof.insert(0, nodoactual)
            nodoactual = path[nodoactual]

        except KeyError:
            print('No existe un camino')
            break
    caminof.insert(0,inicio)

    if distanciamin[meta] != n:
        print('La distancia mas corta es de ' + str(distanciamin[meta]) +' y el camino es '+ str(caminof))
dijkstra(grafica, 'A', 'I')