import math
import argparse


def servidores_minimos(disponibilidade_alvo, p):
    if not (0 < disponibilidade_alvo < 1):
        raise ValueError("A disponibilidade alvo deve estar entre 0 e 1 (exclusivo).")
    if not (0 < p < 1):
        raise ValueError("p deve estar entre 0 e 1 (exclusivo).")

    # Caso k=1: A = 1 - (1-p)^n  =>  n >= log(1-A) / log(1-p)
    n_real = math.log(1 - disponibilidade_alvo) / math.log(1 - p)
    n_minimo = max(1, math.ceil(n_real))
    return n_minimo


def disponibilidade_obtida(n, p):
    return 1 - ((1 - p) ** n)


def imprimir_tabela(alvos, p):
    print(f"Probabilidade individual p = {p:.4f}")
    print("Disponibilidade alvo | Servidores (n) | Replicas adicionais | Disponibilidade obtida")
    print("-" * 86)

    for alvo in alvos:
        n = servidores_minimos(alvo, p)
        replicas_adicionais = n - 1
        obtida = disponibilidade_obtida(n, p)
        print(f"{alvo:20.6f} | {n:14d} | {replicas_adicionais:20d} | {obtida:22.8f}")


def main():
    parser = argparse.ArgumentParser(
        description="Calcula quantas replicas sao necessarias para atingir disponibilidade alvo (k=1)."
    )
    parser.add_argument("--p", type=float, default=0.5, help="Probabilidade de cada servidor estar ativo.")
    parser.add_argument(
        "--alvos",
        type=float,
        nargs="+",
        default=[0.9, 0.99, 0.999, 0.9999, 0.99999, 0.999999],
        help="Lista de disponibilidades alvo.",
    )

    args = parser.parse_args()
    imprimir_tabela(args.alvos, args.p)


if __name__ == "__main__":
    main()