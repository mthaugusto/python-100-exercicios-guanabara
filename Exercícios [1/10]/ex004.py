# [4 / 100] Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

var = input("Insira aqui qualquer coisa: ")

print(f"O tipo primitivo de {var} é: {type(var)}.")
print('Só tem espaços?', var.isspace())
print('É um número?', var.isnumeric())
print('É alfabetico?', var.isalpha())
print('É alfanum[erico?', var.isalnum())
print('Está em maiúsculas?', var.isupper())
print('Está em minúsculas?', var.islower())
print('Está capitalizada?', var.istitle())