from collections import deque
import random

def quicksort_iterativo(lista):
    """Ordena a lista usando o algoritmo de quicksort iterativo com deque"""
    if len(lista) <= 1:
        return lista
    pilha = deque([(0, len(lista) - 1)])
    while pilha:
        esquerda, direita = pilha.pop()
        if esquerda >= direita:
            continue
        pivo = lista[direita]
        i = esquerda - 1
        for j in range(esquerda, direita):
            if lista[j] <= pivo:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
        lista[i+1], lista[direita] = lista[direita], lista[i+1]
        pilha.append((esquerda, i))
        pilha.append((i+2, direita))
    return lista


lista_aleatoria = random.sample(range(100), 10)
print(lista_aleatoria)
print(quicksort_iterativo(lista_aleatoria))
