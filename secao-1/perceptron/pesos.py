"""
Modelo de problema

A   B   S
0   0   0
0   1   0
1   0   0
1   1   1

re -> resposta esperada
rc -> resposta calculada
tax_aprend = taxa de aprendizagem
"""

import numpy as np


tax_aprend = 0.90


def soma(a, b):
    # soma = 0
    # for i in range(len(a)):
    #     soma += a[i]*b[i]
    # return soma
    return np.dot(a, b)


def ativacao(param):
    return 1 if param > 1 else 0


def erro(re, rc):
    return re - rc


def ajuste_peso(p, tax_aprend, e, erro):
    return p + (tax_aprend*e*erro)


s = soma([0, 0, 1, 1, ], [0, 0, 1, 1])
print(ativacao(s))
