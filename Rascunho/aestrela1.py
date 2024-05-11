import numpy as np
from queue import PriorityQueue
from pyamaze import maze, agent
from scipy.spatial import distance
import networkx as nx 

destino = (3,3)

def h_score(celula_atual, destino):
    linha_atual, coluna_atual = celula_atual

    linha_destino, coluna_destino = destino

    #manual
    dist = np.sqrt((linha_destino - linha_atual)**2 + (coluna_destino - coluna_atual)**2)
    #funcao pronta
    dist = distance.euclidean(celula_atual, destino)

    return dist.round()


def aestrela (labirinto):
    f_score = {celula: float("inf") for celula in labirinto.grid}
    g_score = {}
    
    celula_inicial = (0,0)

    g_score[celula_inicial] = 0
    f_score[celula_inicial] = g_score[celula_inicial] + h_score(celula_inicial, destino)

    print(f_score)

    fila = PriorityQueue()
    item = (f_score[celula_inicial], h_score[celula_inicial], celula_inicial)

    fila.put(item)

    while not fila.empty():
        celula = fila.get()[2]

        if celula == destino:
            break

        for direcao in 'NSEW':
        
        
            pass
    
    pass

labirinto = maze()

labirinto.CreateMaze()

agente = agent(labirinto, filled=True, footprints=True)
#caminho = {(10,10):(9,9)}

#labirinto.tracePath({agente: caminho},delay=300)
aestrela(labirinto)
#labirinto.run() 