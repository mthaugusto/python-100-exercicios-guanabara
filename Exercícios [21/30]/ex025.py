# [25 / 100] Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input("Insira o seu nome completo: ").upper()

if 'SILVA' in nome:
    print("Você possui Silva no nome")
else:
    print("Você não possui Silva no nome")