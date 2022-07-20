"""
Modelo de problema

A   B   S
0   0   0
0   1   0
1   0   0
1   1   1

re -> resposta esperada
rc -> resposta calculada
taxa_aprend = taxa de aprendizagem
"""

import numpy as np

taxa_acerto = 0.95
taxa_aprendizagem = 0.1
valor = 0
geracao = 1

entradas = np.array([0, 0], [0, 1], [1, 0], [1, 1])
saidas = np.array([0, 0, 0, 1])
pesos = np.array([0.0, 0.0])
# pesos = np.array([0.786,0.206,0.076])
print(entradas)
print(pesos)


def step_function(n):
    return 1 if n >= 1 else 0


def calcula_saida(registro):
    s = registro.dot(pesos)
    return step_function(s)


def treinar():
    return 0
