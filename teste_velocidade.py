import numpy as np
import time

entradas = np.array([-1, 7, 5, -4, 6, 5, -10, -1, 7, 5, -4, 6, 5, -10])
pesos = np.array([0.8, 0.1, 0, 0.02, 0.6, -0.74, 0.32,
                 0.8, 0.1, 0, 0.02, 0.6, -0.74, 0.32])
i = [-1, 7, 5, -4, 6, 5, -10, -1, 7, 5, -4, 6, 5, -10]
w = [0.8, 0.1, 0, 0.02, 0.6, -0.74, 0.32, 0.8, 0.1, 0, 0.02, 0.6, -0.74, 0.32]


def somatoria(entradas=[], pesos=[]):
    soma = 0
    comb = zip(entradas, pesos)
    for item in comb:
        print(item[0]+item[1])
        soma += item[0]*item[1]
    return soma


def soma(e, p):
    return np.dot(e, p)


inicio_somatoria = time.time()

somatoria(i, w)

fim_somatoria = time.time()

inicio_soma = time.time()

soma(entradas, pesos)

fim_soma = time.time()

print((fim_somatoria-inicio_somatoria) * 10000000000000)
print((fim_soma-inicio_soma)*10000000000000)
