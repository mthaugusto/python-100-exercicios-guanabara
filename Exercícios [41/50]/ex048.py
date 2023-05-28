# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500

soma = 0

for num in range (1, 501):
    if num % 2 != 0 and num % 3 == 0:
        soma += num

print(soma)