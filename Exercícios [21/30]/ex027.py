# [27 / 100] Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input("Digite seu nome completo: ")
nome_dividido = nome.split()
primeiro_nome = nome_dividido[0]
ultimo_nome = nome_dividido[-1]

print(f"Primeiro nome é: {primeiro_nome}\nÚltimo nome é: {ultimo_nome}")
