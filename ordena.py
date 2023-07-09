# Luiz Sérgio Samico Maciel Filho - 202204940042
# Luis Felipe Fernandes Cardoso - 202204940013

import random
import timeit
from collections import deque


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
                    self.vetor.insert(0, cursor)
            # random
            case 2:
                for i in range(self.qtd):
                    n = random.sample(range(self.qtd), self.qtd)
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
        return f"""        
        {"Algoritmo:":25} {self.algoritmo: <25}
        {"Número de comparações:":25} {self.n_comparacoes: <25}
        {"Número de trocas:":25} {self.n_trocas: <25}
        {"Tempo de execução (s):":25} {self.tempo_exec: <25}
        """

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
                if len(exemplo.vetor) <= 1:
                    return exemplo.vetor
                pilha = deque([(0, len(exemplo.vetor) - 1)])
                while pilha:
                    esquerda, direita = pilha.pop()
                    self.n_comparacoes += 1
                    if esquerda >= direita:
                        continue
                    pivo = exemplo.vetor[direita]
                    i = esquerda - 1
                    for j in range(esquerda, direita):
                        self.n_comparacoes += 1
                        if exemplo.vetor[j] <= pivo:
                            i += 1
                            exemplo.vetor[i], exemplo.vetor[j] = exemplo.vetor[j], exemplo.vetor[i]
                            self.n_trocas += 1
                    exemplo.vetor[i+1], exemplo.vetor[direita] = exemplo.vetor[direita], exemplo.vetor[i+1]
                    self.n_trocas += 1
                    pilha.append((esquerda, i))
                    pilha.append((i+2, direita))
                finish = timeit.default_timer()
                self.tempo_exec = finish - start


#############################################
algoritmo_dict = {1: "bubblesort",
                    2: "quicksort"}

ordem_dict = {1: "descentente",
              2: "aleatória"}

print("""\nEste programa vai realizar três tarefas principais:
      * Gerar um vetor com com números aleatórios de tamanho n.
      * Organizar os elementos utilizando bubblesort ou quicksort (escolha do usuário).
      * Escrever no console a performance do algoritmo.""")
print(f"{'':=<79}")

print("Escolha o número de elementos do vetor de teste (digite o número correspondente):")
n_elementos = int(input(f"""      1. dez
      2. cem
      3. mil
      4. dez mil\nSua escolha: """))

ordenacao = int(input(f"""O vetor deve ser totalmente aleatório, ou em ordem descendente?
      1. Ordem descendente
      2. Aleatório\nSua escolha: """))

algoritmo = int(input(f"""Escolha o algoritmo de ordenação que deseja utilizar:
      1. Bubblesort
      2. Quicksort\nSua escolha: """))

print(f"Você vai ordenar um vetor de tamanho {10**n_elementos} organizado de maneira {ordem_dict[ordenacao]} utilizando {algoritmo_dict[algoritmo]}.")
exemplo_teste = Exemplo(10**n_elementos, ordenacao)
exemplo_teste.gerar()
exemplo_teste_cp = Exemplo(10**n_elementos, ordenacao)
exemplo_teste_cp.gerar()
exemplo_teste_cp.vetor = exemplo_teste.vetor.copy()
print("Vetor gerado:", exemplo_teste)
ordenador = Ordenador(algoritmo)
ordenador.ordenar(exemplo_teste)
comparacao = int(input("Você deseja comparar a performance com o algoritmo alternativo?\n  0. Não\n  1. Sim\nSua escolha: "))

print(f"{'':=<79}")
print("Vetor ordenado:")
print(exemplo_teste)
print(f"\nPerformance:{ordenador.performance()}")

if comparacao:
    ordenador_comp = Ordenador(1 + (algoritmo%2))
    ordenador_comp.ordenar(exemplo_teste_cp)
    print(f"\nPerformance comparativa:{ordenador_comp.performance()}")
