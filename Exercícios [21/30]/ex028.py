# [28 / 100] Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

numero_aleatorio = random.randint(0, 5)
numero_usuario = int(input("Digite um número inteiro de 0 a 5: "))

if numero_usuario == numero_aleatorio:
    print("Parabéns, você acertou o número!")
else:
    print("Você perdeu!")

print(f"Número escolhido pelo usuário: {numero_usuario}")
print(f"Número escolhido pelo computador: {numero_aleatorio}")