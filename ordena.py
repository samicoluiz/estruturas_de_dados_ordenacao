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
    def __init__(self, exemplo, escolha_algoritmo):
        self.vetor = exemplo
        self.algoritmo = Ordenador.algoritmo_dict[escolha_algoritmo]
        self.n_comparacoes = 0
        self.n_trocas = 0
        self.tempo_exec = 0

    def __str__(self):
        return f"""
        {"Vetor ordenado:":25} {self.vetor.vetor}
        {"Algoritmo:":25} {self.algoritmo: <25}
        {"Número de comparações:":25} {self.n_comparacoes: <25}
        {"Número de trocas:":25} {self.n_trocas: <25}
        {"Tempo de execução (s):":25} {self.tempo_exec: <25}
        """

    def _rearranjo(self, esquerda, direita):
        vetor = self.vetor.vetor
        idx_troca = esquerda
        idx_pivo = direita
        for idx_cursor in range(esquerda, direita+1):
            if vetor[idx_cursor] <= vetor[idx_pivo]:
                if idx_cursor > idx_troca:
                    vetor[idx_cursor], vetor[idx_troca] = vetor[idx_troca], vetor[idx_cursor]
                idx_troca += 1

        return idx_troca - 1
    
    def _particionar(self, pivo, esquerda, direita):
        if len(self.vetor.vetor[esquerda:direita+1]) == 1:
            return
        
        if pivo > esquerda + 1: #Confirmação de que o pivo não é o primeiro elemento e já confirmando quando o valor for unitário.
            pivo1 = self._rearranjo(esquerda, pivo-1)
            self._particionar(pivo1, esquerda, pivo-1)
        if pivo + 1 < direita: #Confirmação de que o pivo não é o último elemento e já confirmando quando o valor for unitário.
            pivo2 = self._rearranjo(pivo+1, direita)
            self._particionar(pivo2, pivo+1, direita)

    def ordenar(self):
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
                    for i in range(self.vetor.qtd - 1):
                        self.n_comparacoes += 1
                        if self.vetor.vetor[i] > self.vetor.vetor[i+1]:
                            self.vetor.vetor[i], self.vetor.vetor[i+1] = self.vetor.vetor[i+1], self.vetor.vetor[i]
                            self.n_trocas += 1
                            troca = True
                finish = timeit.default_timer()
                self.tempo_exec = finish - start

            case "quicksort":
                direita = self.vetor.qtd - 1
                esquerda = 0
                pivo = self._rearranjo(esquerda, direita)
                self._particionar(pivo, esquerda, direita)

#############################################
exemplo_teste = Exemplo(5, 2)
exemplo_teste.gerar()
print(exemplo_teste)
# ordenador = Ordenador(exemplo_teste, 1)
# ordenador.ordenar()
# print(exemplo_teste)
# print(ordenador)
# exemplo_teste.vetor = [2, 5, 5, 0, 0]
ordenador2 = Ordenador(exemplo_teste, 2)
ordenador2.ordenar()
print(exemplo_teste)
print(ordenador2)
