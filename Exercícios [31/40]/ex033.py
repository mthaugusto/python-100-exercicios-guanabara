# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
num3 = float(input("Insira o terceiro número: "))

# Método 1 - usando a lógica de programação:  

maior = num1
menor = num1

if num2 > num1 and num2 > num3:
    maior = num2

if num3 > num1 and num3 > num2:
    maior = num3
    
if num2 < num1 and num2 < num3:
    menor = num2

if num3 < num1 and num3 < num2:
    menor = num3

print(f"O maior número é o {maior} e o menor é o {menor}")

# Método 2 - usando as funções min() e max():

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

print(f"O maior número é {maior} e o menor número é {menor}")