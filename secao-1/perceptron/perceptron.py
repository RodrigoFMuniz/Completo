from functools import reduce


i = [1, -2, 3, 4, 5, -6, 1]
w = [-6, -5, -4, -3, 2, 1, 10]


def somatoria(entradas=[], pesos=[]):
    soma = 0
    if len(entradas) == 0 or len(pesos) == 0:
        return 0
    comb = zip(entradas, pesos)
    print(comb.__class__)
    for item in comb:
        print(item[0]+item[1])
        soma += item[0]*item[1]
    print(soma)
    return soma


def ativacao_step_function(n):
    if n > 0:
        return 1
    return 0

# def novo_peso(n):
#     return n *


print(ativacao_step_function(somatoria(i, w)))
