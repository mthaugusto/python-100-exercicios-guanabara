
# [23 / 100] Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input("Digite um número entre 0 e 9999: "))

milhar = num // 1000 # Aqui nós usamos o operador de divisão inteira, que arredonda para baixo. Ex - 1387 // 1000 = 1
resto = num % 1000 # Aqui usamos o operador de resto. 1387 % 1000 = 387
centena = resto // 100 # Aqui usamos o operador de divisão inteira novamente para pegar a centena do resto. 387 // 100 = 3
resto = resto % 100 # Mais uma vez calculamos o resto para pegar as dezenas. 387 % 100 = 87
dezena = resto // 10 # Operador de divisão initeira para pegar a casa da dezena. 87 // 10 = 8
unidade = resto % 10 # Calculamos o resto de 87 % 10 = 7 

print(f"Milhar: {milhar}")
print(f"Centena: {centena}")
print(f"Dezena: {dezena}")
print(f"Unidade: {unidade}")
