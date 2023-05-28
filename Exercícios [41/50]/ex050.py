# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsedere-o

soma = 0 

for x in range(6):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        soma += num

print(soma)