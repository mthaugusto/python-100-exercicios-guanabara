# [18 / 100] Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input("Digite o valor do ângulo em graus: "))

# Converter o ângulo de graus para radianos
angulo_rad = math.radians(angulo)

# Calcular o seno, cosseno e tangente
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

print(f"O valor do seno é: {seno}\nO valor do cosseno é: {cosseno}\nO valor da tangente é: {tangente}")