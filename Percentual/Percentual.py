# Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação
# que cada estado teve dentro do valor total mensal da distribuidora.

from prettytable import PrettyTable

# Variaveis

estados_faturamento = [
    {
        "Estado": "SP",
        "Faturamento": 67836.43
    },
    {
        "Estado": "RJ",
        "Faturamento": 36678.66
    },
    {
        "Estado": "MG",
        "Faturamento": 29229.88
    },
    {
        "Estado": "ES",
        "Faturamento": 27165.48
    },
    {
        "Estado": "Outros",
        "Faturamento": 19849.53
    }
]

total = sum(e["Faturamento"] for e in estados_faturamento)

# Tabela

tabela = PrettyTable()
tabela.field_names = ["Estado", "Faturamento", "Porcentagem"]

# Obter porcentagens

for estado in estados_faturamento:
    porcentagem = round((estado["Faturamento"] * 100) / total, 1)
    tabela.add_row([estado["Estado"], estado["Faturamento"], porcentagem])

# Imprimir resultados

print(tabela)
