# Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa,
# na linguagem que desejar, que calcule e retorne:

# * O menor valor de faturamento ocorrido em um dia do mês;
# * O maior valor de faturamento ocorrido em um dia do mês;
# * Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:

# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json
from prettytable import PrettyTable

# Principais variaveis
faturamentos = []
dias_superou_media = []

menor_receita = 0
maior_receita = 0
media_receita = 0


# Criando tabela e seus campos
tabela = PrettyTable()
tabela.field_names = ["Dia", "Semana", "Faturamento", "Feriado"]

# Selecionando o mes

print("1 - Janeiro \n2 - Fevereiro \n3 - Março")

selecao = int(input("Selecione um mês: "))

if selecao == 1:
    selecao = "janeiro"
elif selecao == 2:
    selecao = "fevereiro"
elif selecao == 3:
    selecao = "marco"
else:
    print("Valor invalido!")

print(f"Informações do mês {selecao}")

# Puxando o arquivo JSON
with open('./faturamento.json', 'r') as arquivo:
    
    dados = json.load(arquivo)

# Pegando informacoes do mes selecionado
for dado in dados[selecao]:

    if dado["faturamento"] != 0:
        if dado["feriado"]:
            tabela.add_row([dado["dia"], dado["semana"], dado["faturamento"], "Sim"])
        else:
            tabela.add_row([dado["dia"], dado["semana"], dado["faturamento"], "Não"])
        faturamentos.append({ "faturamento": dado["faturamento"], "dia": dado["dia"]})
        media_receita = media_receita + dado["faturamento"]
    else:
        if dado["feriado"]:
            tabela.add_row([dado["dia"], dado["semana"], "---", "Sim"])
        else:
            tabela.add_row([dado["dia"], dado["semana"], "---", "Não"])

# Buscando pelo menor, maior e a media dos faturamentos

menor_receita = min(faturamentos, key=lambda x: x['faturamento'])
maior_receita = max(faturamentos, key=lambda x: x['faturamento'])
media_receita = round(media_receita / len(faturamentos), 2)

for fatura in faturamentos:
    if fatura["faturamento"] > media_receita:
        dias_superou_media.append(fatura)

# Exibindo todos os resultados em tela

print(tabela)

print(f"Sua maior receita foi no dia {maior_receita['dia']} - {maior_receita['faturamento']}")
print(f"Sua menor receita foi no dia {menor_receita['dia']} - {menor_receita['faturamento']}")
print(f"Sua média foi de: {media_receita}")
print(f"Dias acima da media: ")

for dia in dias_superou_media:
    print(f"    {dia['dia']} - {dia['faturamento']}")
