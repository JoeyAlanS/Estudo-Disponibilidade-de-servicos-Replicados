import random

def simulador(n, k, p, rodadas=100000):

    sucesso = 0

    for _ in range(rodadas):

        ativos = 0

        for _ in range(n):

            if random.random() <= p:
                ativos += 1

        if ativos >= k:
            sucesso += 1

    return sucesso / rodadas


n = 5
k = 3
p = 0.9

resultado = simulador(n,k,p)

print("Disponibilidade simulada:",resultado)