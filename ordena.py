# Luiz Sérgio Samico Maciel Filho - 202204940042
# Luis Felipe Fernandes Cardoso - 202204940013

import random
import timeit


class Exemplo:
    """Cria uma estrutura de dados contendo números inteiros aleatórios"""
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

    algoritmo_dict = {1: "bubblesort",
                      2: "quicksort"}

    """Objeto ordenador para um vetor de exemplo"""
    def __init__(self,  escolha_algoritmo):
        # self.vetor = exemplo
        self.algoritmo = Ordenador.algoritmo_dict[escolha_algoritmo]
        self.n_comparacoes = 0
        self.n_trocas = 0
        self.tempo_exec = 0

    def performance(self):
        print(f"""
        
        {"Algoritmo:":25} {self.algoritmo: <25}
        {"Número de comparações:":25} {self.n_comparacoes: <25}
        {"Número de trocas:":25} {self.n_trocas: <25}
        {"Tempo de execução (s):":25} {self.tempo_exec: <25}
        """)

    def _rearranjo(self, exemplo, esquerda, direita):
        idx_troca = esquerda
        idx_pivo = direita
        for idx_cursor in range(esquerda, direita+1):
            if exemplo.vetor[idx_cursor] <= exemplo.vetor[idx_pivo]:
                self.n_comparacoes += 1
                if idx_cursor > idx_troca:
                    self.n_comparacoes += 1
                    exemplo.vetor[idx_cursor], exemplo.vetor[idx_troca] = exemplo.vetor[idx_troca], exemplo.vetor[idx_cursor]
                    self.n_trocas += 1
                idx_troca += 1
        return idx_troca - 1

    def _particionar(self, exemplo, pivo, esquerda, direita):
        if esquerda > direita:
            return

        pivo1 = self._rearranjo(exemplo, esquerda, pivo-1)
        self._particionar(exemplo, pivo1, esquerda, pivo-1)
        pivo2 = self._rearranjo(exemplo, pivo+1, direita)
        self._particionar(exemplo, pivo2, pivo+1, direita)

    def ordenar(self, exemplo):
        """Ordena o algoritmo usando o algoritmo de bubblesort ou quicksort"""
        match self.algoritmo:
            case "bubblesort":
                # Iniciando o temporizador
                start = timeit.default_timer()
                # Criando variável para garantir que o vetor vai ser percorrido
                # pelo menos uma vez. Simulacro do DO WHILE.
                primeira_passagem = True
                troca = False
                while troca or primeira_passagem:
                    if primeira_passagem:
                        primeira_passagem = False
                    troca = False
                    for i in range(exemplo.qtd - 1):
                        self.n_comparacoes += 1
                        if exemplo.vetor[i] > exemplo.vetor[i+1]:
                            exemplo.vetor[i], exemplo.vetor[i+1] = exemplo.vetor[i+1], exemplo.vetor[i]
                            self.n_trocas += 1
                            troca = True
                finish = timeit.default_timer()
                self.tempo_exec = finish - start

            case "quicksort":
                start = timeit.default_timer()
                direita = exemplo.qtd - 1
                esquerda = 0
                pivo = self._rearranjo(exemplo, esquerda, direita)
                self._particionar(exemplo, pivo, esquerda, direita)
                finish = timeit.default_timer()
                self.tempo_exec = finish - start


#############################################
exemplo_teste = Exemplo(100, 2)
exemplo_teste.gerar()
print(exemplo_teste)
# ordenador = Ordenador(exemplo_teste, 1)
# ordenador.ordenar()
# print(exemplo_teste)
# print(ordenador)
# exemplo_teste.vetor = [2, 5, 5, 0, 0]
ordenador2 = Ordenador(2)
ordenador2.ordenar(exemplo_teste)
print(exemplo_teste)
ordenador2.performance()

#############################################
algoritmo_dict = {1: "bubblesort",
                    2: "quicksort"}


print("""Este programa vai realizar três tarefas principais:
      * Gerar um vetor com com números aleatórios de tamanho n.
      * Organizar os elementos utilizando bubblesort ou quicksort (escolha do usuário).
      * Escrever no console a performance do algoritmo.""")
print(f"{'':=<79}")
print("Escolha o número de elementos do vetor desordenado (digite o número correspondente):")
n_elementos = int(input(f"""      1. dez
      2. cem
      3. mil
      4. dez mil\nSua escolha: """))
algoritmo = int(input(f"""Escolha o algoritmo de ordenação que deseja utilizar:
      1. Bubblesort
      2. Quicksort\nSua escolha: """))
print(f"Você vai ordenar um vetor de tamanho {10**n_elementos} utilizando {algoritmo_dict[algoritmo]}.")
