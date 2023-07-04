# Luiz Sérgio Samico Maciel Filho - 202204940042
# Luis Felipe Fernandes Cardoso - 202204940013

import random
import timeit


class Exemplo:
    """Cria uma estrutura de dados contendo numeros inteiros aleatorios"""
    def __init__(self, qtd, ordenacao):
        self.qtd = qtd
        self.ordenacao = ordenacao
        self.vetor = []

    def __str__(self):
        return f"{self.vetor}"

    def gerar(self):
        """Gera os números em ordem crescente ou aleatoriamente"""        
        cursor = random.randint(0, self.qtd)
        match self.ordenacao:
            # descendente
            case 1:
                for i in range(self.qtd):
                    cursor = random.randint(cursor, self.qtd + cursor)
                    self.vetor.append(cursor)
            # random
            case 2:
                for i in range(self.qtd):
                    n = random.randint(0, self.qtd)
                    self.vetor.append(n)


class Ordenador:
    """Objeto ordenador para um vetor de exemplo"""

    def __init__(self, exemplo, algoritmo):
        self.vetor = exemplo
        self.algoritmo = algoritmo
        self.n_comparacoes = None
        self.n_trocas = None
        self.tempo_exec = None

    def ordenar(self):
        """Ordena o algoritmo usando o algoritmo de bubblesort ou quicksort"""
        match self.algoritmo:
            # bubblesort
            case 1:
                pass
            # quicksort
            case 2:
                pass


exemplo_teste = Exemplo(10, 2)
exemplo_teste.gerar()
print(exemplo_teste)
