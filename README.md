# 🔴 Target-Sistemas
Este é um repositório explicando os desafios e os processos que utilizei para resolver os desafios da Target Sistemas.
<p>Linguagem utilizada: Python🟡🔵</p>

## 🌻 Desafio Fibonacci

####Enunciado:

```
  Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
  (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
  ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
  
  IMPORTANTE:
  Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
```

####Código:

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

####Referência:
```
https://www.educamaisbrasil.com.br/enem/matematica/sequencia-de-fibonacci
```
#### Minhas considerações

Nesse desafio tive que estudar um pouco sobre a Sequência de Fibonacci, mas sem muitas dificuldades. Depois que aprendi a fórmula bastou aplica-la

## 🧷 Desafio Faturamento

####Enunciado:

```
  Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa,
  na linguagem que desejar, que calcule e retorne:
  
  <ul>
    <li>O menor valor de faturamento ocorrido em um dia do mês;</li>
  </ul>
```

## 📊 Desafio Percentual

## 🔀 Desafio Inverter String
 
