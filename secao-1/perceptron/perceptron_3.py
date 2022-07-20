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


def soma(e, p):
    return np.dot(e, p)


def step_function(n):
    return 1 if n >= 1 else 0


def ajuste_peso(e, err, peso, taxa_aprendizagem):
    return peso + (taxa_aprendizagem*e*err)


def calc_err(pesos):
    return


while valor < taxa_acerto:
    print(f'Geração: {geracao}')
    s = soma(entradas, pesos)
    sf = step_function(s)
    print(f'Valor da stepfunction {sf}')
    if sf >= 1:
        print(f'Resultado atingido na geração: {geracao}')
        valor = sf
    else:
        for ind, p in enumerate(pesos):
            pesos[ind] = ajuste_peso(entradas[ind], 0.15, p, taxa_aprendizagem)
            print(f'Geração {geracao} => Novo peso {ind}: {pesos[ind]}')
        geracao += 1
        if geracao == 1000:
            break
