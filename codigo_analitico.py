import math

def disponibilidade(n, k, p):
    if n <= 0:
        raise ValueError("n deve ser maior que 0")
    if not (0 < k <= n):
        raise ValueError("k deve satisfazer 0 < k <= n")
    if not (0 <= p <= 1):
        raise ValueError("p deve satisfazer 0 <= p <= 1")

    total = 0.0
    for i in range(k, n + 1):
        combinacao = math.comb(n, i)
        prob = combinacao * (p ** i) * ((1 - p) ** (n - i))
        total += prob
    return total


def demonstracao_analitica():
    ns = [1, 2, 3, 5, 7, 10]
    ps = [0.5, 0.8, 0.9]

    print("n | caso | k | p | disponibilidade")
    print("-" * 52)

    for p in ps:
        for n in ns:
            casos = [
                ("k=1", 1),
                ("k=ceil(n/2)", math.ceil(n / 2)),
                ("k=n", n),
            ]
            for caso, k in casos:
                a = disponibilidade(n, k, p)
                print(f"{n:2d} | {caso:11s} | {k:2d} | {p:.1f} | {a:.8f}")


if __name__ == "__main__":
    demonstracao_analitica()