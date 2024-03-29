#
# Implementa um min-heap
# (uma arvore binaria em que o menor elemento sempre esta na raiz)
#
# Elementos devem ser objetos que sao comparados pela propriedade (variavel) f
#
# Ref.: "Introduction to Algorithms" - Cormen, Leiserson, Rivest & Stein
# 3rd edition, MIT Press, 2009.
#

class MinHeap:
    def __init__(self):
        self.contents = []
        self.capacity = 0
        self.size = 0

    # remove o menor elemento do heap e reestabelece a ordem correta
    def remove_min(self):
        if self.size < 1:
            return None 
        
        # guarda o menor elemento e coloca o ultimo elemento na raiz
        minimo = self.contents[0]
        self.contents[0] = self.contents[self.size-1]
        self.size -= 1

        # reestabelece a propriedade do min-heap
        self.__min_heapify(0)

        return minimo

    def adiciona(self, node):
        indice = self.size 
        if self.capacity == self.size:
            self.contents.append(node)
            self.capacity += 1
        self.__insert(indice, node)
        self.size += 1


    # Metodos privados
    def __pai(self, i):
        return (i - 1) // 2

    def __filho_esquerdo(self, i):
        return i * 2 + 1

    def __filho_direito(self, i):
        return i * 2 + 2

    def __swap(self, i, j):
        self.contents[i], self.contents[j] = self.contents[j], self.contents[i]

    def __min_heapify(self, i):
        l = self.__filho_esquerdo(i)
        r = self.__filho_direito(i)

        # encontra qual o menor dos tres nos: i, l ou r
        minimo = i 

        if l < self.size and self.contents[i].f > self.contents[l].f:
            minimo = l 

        if r < self.size and self.contents[minimo].f > self.contents[r].f:
            minimo = r 

        # se i nao for o menor no, troca de lugar com o menor e continua
        # recursivamente
        if minimo != i:
            self.__swap(i, minimo)
            self.__min_heapify(minimo)

    def __insert(self, i, node):
        self.contents[i] = node 
        while i > 0 and self.contents[self.__pai(i)].f > self.contents[i].f:
            self.__swap(i, self.__pai(i))
            i = self.__pai(i)


# uma fila de prioridade que retorna os nos de valor minimo primeiro
class PriorityQueue:
    def __init__(self):
        self.heap = MinHeap()

    def remove_min(self):
        self.heap.remove_min()

    def adiciona(self, node):
        self.heap.adiciona(node)


# Ordena uma lista de numeros usando um heap, 
# para testar a implementacao
def heap_sort(numeros):
    heap = MinHeap()

    class NoNumerico:
        def __init__(self, n):
            self.f = n

    for num in numeros:
        heap.adiciona(NoNumerico(num))

    resultado = []
    while heap.size > 0:
        n = heap.remove_min()
        resultado.append(n.f)

    return resultado 
