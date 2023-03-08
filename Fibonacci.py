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
    

# Referência: https://www.educamaisbrasil.com.br/enem/matematica/sequencia-de-fibonacci