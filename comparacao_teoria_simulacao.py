import csv
import math
import random
from pathlib import Path

import matplotlib.pyplot as plt


def disponibilidade(n, k, p):
    if n <= 0:
        raise ValueError("n deve ser maior que 0")
    if not (0 < k <= n):
        raise ValueError("k deve satisfazer 0 < k <= n")
    if not (0 <= p <= 1):
        raise ValueError("p deve satisfazer 0 <= p <= 1")

    total = 0.0
    for i in range(k, n + 1):
        total += math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
    return total


def simulador(n, k, p, rodadas=100000):
    sucesso = 0
    for _ in range(rodadas):
        ativos = sum(1 for _ in range(n) if random.random() <= p)
        if ativos >= k:
            sucesso += 1
    return sucesso / rodadas


def calcular_k(caso, n):
    if caso == "k=1":
        return 1
    if caso == "k=ceil(n/2)":
        return math.ceil(n / 2)
    if caso == "k=n":
        return n
    raise ValueError(f"Caso desconhecido: {caso}")


def gerar_resultados(n_inicio, n_fim, p_valores, rodadas):
    casos = ["k=1", "k=ceil(n/2)", "k=n"]
    resultados = []
    for p in p_valores:
        for n in range(n_inicio, n_fim + 1):
            for caso in casos:
                k = calcular_k(caso, n)
                analitico = disponibilidade(n, k, p)
                simulado = simulador(n, k, p, rodadas=rodadas)
                erro_abs = abs(analitico - simulado)
                resultados.append(
                    {
                        "n": n,
                        "caso": caso,
                        "k": k,
                        "p": p,
                        "analitico": analitico,
                        "simulado": simulado,
                        "erro_abs": erro_abs,
                    }
                )
    return resultados


def salvar_csv(resultados, caminho_csv):
    with caminho_csv.open("w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(
            arquivo,
            fieldnames=["n", "caso", "k", "p", "analitico", "simulado", "erro_abs"],
        )
        escritor.writeheader()
        for linha in resultados:
            escritor.writerow(linha)


def plotar_analitico_por_caso(resultados, p_grafico, caminho_figura):
    plt.figure(figsize=(9, 5))
    for caso in ["k=1", "k=ceil(n/2)", "k=n"]:
        pontos = [r for r in resultados if r["caso"] == caso and r["p"] == p_grafico]
        ns = [r["n"] for r in pontos]
        ys = [r["analitico"] for r in pontos]
        plt.plot(ns, ys, marker="o", label=f"Analitico ({caso})")

    plt.xlabel("n")
    plt.ylabel("Disponibilidade")
    plt.title(f"Disponibilidade analitica para casos base (p={p_grafico})")
    plt.ylim(0, 1.02)
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(caminho_figura, dpi=150)
    plt.close()


def plotar_teoria_vs_simulacao(resultados, p_grafico, caminho_figura):
    plt.figure(figsize=(10, 6))
    for caso in ["k=1", "k=ceil(n/2)", "k=n"]:
        pontos = [r for r in resultados if r["caso"] == caso and r["p"] == p_grafico]
        ns = [r["n"] for r in pontos]
        analitico = [r["analitico"] for r in pontos]
        simulado = [r["simulado"] for r in pontos]

        plt.plot(ns, analitico, label=f"Analitico ({caso})")
        plt.plot(ns, simulado, "--", label=f"Simulado ({caso})")

    plt.xlabel("n")
    plt.ylabel("Disponibilidade")
    plt.title(f"Comparacao entre teoria e simulacao (n=1..20, p={p_grafico})")
    plt.ylim(0, 1.02)
    plt.grid(alpha=0.3)
    plt.legend(ncol=2)
    plt.tight_layout()
    plt.savefig(caminho_figura, dpi=150)
    plt.close()


def imprimir_resumo(resultados):
    print("n | caso | k | p | analitico | simulado | erro_abs")
    print("-" * 72)
    for r in resultados:
        print(
            f"{r['n']:2d} | {r['caso']:11s} | {r['k']:2d} | {r['p']:.2f} | "
            f"{r['analitico']:.8f} | {r['simulado']:.8f} | {r['erro_abs']:.8f}"
        )

    erro_maximo = max(resultados, key=lambda r: r["erro_abs"])
    print("\nMaior erro absoluto:")
    print(
        f"p={erro_maximo['p']:.2f}, n={erro_maximo['n']}, caso={erro_maximo['caso']}, "
        f"erro_abs={erro_maximo['erro_abs']:.8f}"
    )


if __name__ == "__main__":
    random.seed(42)

    n_inicio = 1
    n_fim = 20
    p_valores = [0.5, 0.8, 0.9]
    p_grafico = 0.9
    rodadas = 50000

    resultados = gerar_resultados(n_inicio, n_fim, p_valores, rodadas)

    base = Path(__file__).resolve().parent
    caminho_csv = base / "tabela_teoria_vs_simulacao.csv"
    caminho_analitico = base / "grafico_disponibilidade_analitica.png"
    caminho_comparacao = base / "grafico_teoria_vs_simulacao.png"

    salvar_csv(resultados, caminho_csv)
    plotar_analitico_por_caso(resultados, p_grafico, caminho_analitico)
    plotar_teoria_vs_simulacao(resultados, p_grafico, caminho_comparacao)
    imprimir_resumo(resultados)

    print("\nArquivos gerados:")
    print(f"- {caminho_csv.name}")
    print(f"- {caminho_analitico.name}")
    print(f"- {caminho_comparacao.name}")