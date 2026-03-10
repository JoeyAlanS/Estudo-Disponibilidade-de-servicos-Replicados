# Disponibilidade de Serviços Replicados

## GRUPO G

* NOME: Joey Alan de Freitas Solis - MATRÍCULA:2320416
* NOME: Hector Zendejas Rebouças  - MATRÍCULA:2315024

---
## Introdução

Em sistemas distribuídos, a replicação de servidores é utilizada para aumentar a disponibilidade de um serviço. Quando um serviço é replicado em múltiplos servidores, ele pode continuar funcionando mesmo que alguns servidores falhem.

Neste trabalho analisamos matematicamente e experimentalmente a disponibilidade de um serviço replicado.

Os parâmetros considerados são:

* **n** → número total de servidores
* **k** → número mínimo de servidores disponíveis para que o serviço funcione
* **p** → probabilidade de um servidor estar disponível em um determinado instante

Com esses parâmetros é possível calcular a disponibilidade do serviço.

---

# Exercício 1.1 — Dedução da Fórmula

Cada servidor possui probabilidade **p** de estar disponível e probabilidade **(1 − p)** de falhar.

Como cada servidor opera de forma independente, o número de servidores disponíveis segue uma distribuição binomial.

A probabilidade de **exatamente i servidores estarem disponíveis** é dada por:

P(i) = C(n,i) * p^i * (1-p)^(n-i)

onde:

C(n,i) = n! / (i!(n-i)!)

é o coeficiente binomial.

O serviço permanece disponível quando **pelo menos k servidores estão ativos**.

Assim, a disponibilidade do sistema é:

A(n,k,p) = Σ(i=k até n) C(n,i) p^i (1-p)^(n-i)

---

## Casos extremos

### k = 1 (operações de consulta)

O sistema funciona se **ao menos um servidor estiver ativo**.

É mais fácil calcular a probabilidade de todos falharem.

A = 1 - (1 - p)^n

---

### k = n (operações de atualização)

Todos os servidores precisam estar disponíveis.

A disponibilidade é:

A = p^n

---

# Exercício 1.2 — Análise Analítica

Utilizando a fórmula derivada anteriormente, implementamos um programa que calcula a disponibilidade para diferentes valores de **n**, **k** e **p**.

Foram analisados três cenários principais:

* k = 1
* k = n/2
* k = n

Os resultados foram organizados em tabelas e visualizados em gráficos 2D para facilitar a análise.

Observa-se que quanto maior o valor de **k**, menor tende a ser a disponibilidade do sistema, pois mais servidores precisam estar disponíveis simultaneamente.

---

# Exercício 1.2 — Simulação Estocástica

Além do cálculo analítico, foi implementado um simulador estocástico para validar os resultados teóricos.

O simulador funciona da seguinte forma:

1. Define-se os valores de **n**, **k** e **p**
2. Para cada rodada:

   * gera-se um número aleatório entre 0 e 1 para cada servidor
   * se o número for menor ou igual a **p**, o servidor é considerado disponível
3. Conta-se quantos servidores estão ativos
4. Verifica-se se pelo menos **k servidores estão disponíveis**
5. Repete-se o processo por um grande número de rodadas

A disponibilidade experimental é então calculada como:

disponibilidade = rodadas bem sucedidas / total de rodadas

Os resultados experimentais são comparados com os valores analíticos.

Quando o número de rodadas é grande, os valores simulados se aproximam dos valores teóricos.

---

# Conclusão

Os resultados mostram que a replicação de servidores aumenta significativamente a disponibilidade do sistema.

Porém, exigir muitos servidores simultaneamente disponíveis (valores altos de **k**) reduz a disponibilidade geral do serviço.

A simulação estocástica confirmou os valores obtidos pela fórmula analítica, demonstrando a validade do modelo matemático.
