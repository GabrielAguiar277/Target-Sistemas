# 🔴 Target-Sistemas
Este é um repositório explicando os desafios e os processos que utilizei para resolver os desafios da Target Sistemas.
<p>Linguagem utilizada: Python🟡🔵</p>

## 🌻 Desafio Fibonacci

#### Enunciado:

```
  Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
  (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
  ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
  
  IMPORTANTE:
  Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
```

#### Código:

```python
num = int(input("Escolha algum numero inteiro: "))

a = 0
b = 1

while b < num:
    temp = a + b
    a = b
    b = temp

if b == num or num == 0:
    print(f"{num} pertence a sequência de Fibonacci")
    
else:
    print(f"{num} não pertence a sequência de Fibonacci")

```

#### Referência:
```
https://www.educamaisbrasil.com.br/enem/matematica/sequencia-de-fibonacci
```
#### Minhas considerações

Nesse desafio tive que estudar um pouco sobre a Sequência de Fibonacci, mas sem muitas dificuldades. Depois que aprendi a fórmula bastou aplica-la

## 🧷 Desafio Faturamento

#### Enunciado:

```
  Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa,
  na linguagem que desejar, que calcule e retorne:
  
  ▪ O menor valor de faturamento ocorrido em um dia do mês;
  ▪ O maior valor de faturamento ocorrido em um dia do mês;
  ▪ Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
  
  IMPORTANTE:
  
  a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
  b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
  
```

#### Dependências

<p>
  Importante ressaltar que utilizei uma biblioteca para formar tabelas, caso queira rodar por conta própria será necessário instala-la com o comando:
</p>

```bash
  pip install prettytable
```

#### Observações

<p>
  Vale ressaltar também que tomei a liberdade de criar meu próprio json, tentei ao máximo idelizar do jeito que vocês gostariam
</p>

#### Código:

```python

import json
from prettytable import PrettyTable

faturamentos = []
dias_superou_media = []

menor_receita = 0
maior_receita = 0
media_receita = 0

tabela = PrettyTable()
tabela.field_names = ["Dia", "Semana", "Faturamento", "Feriado"]

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

with open('./faturamento.json', 'r') as arquivo:
    
    dados = json.load(arquivo)

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
            
menor_receita = min(faturamentos, key=lambda x: x['faturamento'])
maior_receita = max(faturamentos, key=lambda x: x['faturamento'])
media_receita = round(media_receita / len(faturamentos), 2)

for fatura in faturamentos:
    if fatura["faturamento"] > media_receita:
        dias_superou_media.append(fatura)
        
print(tabela)

print(f"Sua maior receita foi no dia {maior_receita['dia']} - {maior_receita['faturamento']}")
print(f"Sua menor receita foi no dia {menor_receita['dia']} - {menor_receita['faturamento']}")
print(f"Sua média foi de: {media_receita}")
print(f"Dias acima da media: ")

for dia in dias_superou_media:
    print(f"    {dia['dia']} - {dia['faturamento']}")

```

#### Minhas considerações

Nesse desafio tive a oportunidade de aprender sobre expressões de funções lâmbidas, que me foi muito util para pegar a o menor e o maior valor de um array de objetos, como exemplificados nas variáveis menor_receita e maior_receita

## 📊 Desafio Percentual

#### Enunciado:

```
  Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
  
  ▪ SP – R$67.836,43
  ▪ RJ – R$36.678,66
  ▪ MG – R$29.229,88
  ▪ ES – R$27.165,48
  ▪ Outros – R$19.849,53
  
  Escreva um programa na linguagem que desejar onde calcule o percentual de representação
  que cada estado teve dentro do valor total mensal da distribuidora.
  
```

#### Dependências

<p>
  Assim como na atividade do Desafio Faturamento, eu utilizei a biblioteca de tabelas. Portanto, se porventura você quiser executar o código na sua máquina, você deve   executar este comando no seu bash
</p>

```bash
  pip install prettytable
```

#### Código:

```python
  from prettytable import PrettyTable
  
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

tabela = PrettyTable()
tabela.field_names = ["Estado", "Faturamento", "Porcentagem"]

for estado in estados_faturamento:
    porcentagem = round((estado["Faturamento"] * 100) / total, 1)
    tabela.add_row([estado["Estado"], estado["Faturamento"], porcentagem])
    
print(tabela)
```

#### Minhas considerações

Desafio de porcentagem. Escrevi um json que representario o estado e seu respectivo faturamento. Guardei a soma do faturamento de todos os estados o que corresponde a 100%, logo mais para obter a porcentagem de cada estado, multipliquei o valor de faturamento de cada estado e dividi o resultado pelo total(a soma do faturamento de todos os estados). Por fim printei na tela

## 🔀 Desafio Inverter String

#### Enunciado:

```
  Escreva um programa que inverta os caracteres de um string.
  
  IMPORTANTE:
  a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
  b) Evite usar funções prontas, como, por exemplo, reverse;
  
```

#### Código:

```python

  def upsidedown(palavra):

    palavra_final = ""

    for letra in palavra:
        palavra_final = letra + palavra_final 

    return palavra_final
 
palavra = input("Escreva uma palavra: ")
print(upsidedown(palavra))

```

#### Minhas considerações

Nesse desafio, apenas criei uma função que recebe uma palavra, onde logo mais vou interar essa palavra pegando cada letra de forma individual e concatenando com a variável palavra_final, onde logo em seguida será retornada
 
