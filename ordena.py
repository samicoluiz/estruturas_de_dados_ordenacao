# Luiz Sérgio Samico Maciel Filho - 202204940042
# Luis Felipe Fernandes Cardoso - 202204940013

import random
import timeit


class Exemplo:

    def __init__(self, qtd, ordenacao):
        self.qtd = qtd
        self.ordenacao = ordenacao
        self.vetor = []

    def __str__(self):
        return f"{self.vetor}"

    def gerar(self):
        match self.ordenacao:
            case "desc":
                pass
            case "random":
                pass


class Ordenador:

    def __init__(self, exemplo, algoritmo):
        self.vetor = exemplo
        self.algoritmo = algoritmo
        self.n_comparacoes = None
        self.n_trocas = None
        self.tempo_exec = None

    def ordenar(self):
        pass