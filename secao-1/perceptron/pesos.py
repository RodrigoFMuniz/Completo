"""
Modelo de problema

A   B   S
0   0   0
0   1   0
1   0   0
1   1   1
"""

import numpy as np


def soma(a, b):
    # soma = 0
    # for i in range(len(a)):
    #     soma += a[i]*b[i]
    # return soma
    return np.dot(a, b)


s = soma([1, 2, 3], [1, 2, 3])
print(s)
