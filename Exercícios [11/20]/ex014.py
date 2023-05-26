# [14 / 100] Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input("Digite uma temperatura em graus Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print(f"A temperatura de {celsius} °C equivale a {fahrenheit} °F")