# Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua
# preferência ou pode ser previamente definida no código;

# b) Evite usar funções prontas, como, por exemplo, reverse;

# Funcao responsavel pela inversao
def upsidedown(palavra):

    palavra_final = ""

    for letra in palavra:
        palavra_final = letra + palavra_final 

    return palavra_final

# Pega palavra do usuario
palavra = input("Escreva uma palavra: ")

# Imprime o resultado na tela
print(upsidedown(palavra))