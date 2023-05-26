# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - o primeiro valor é mmaior
# - o segundo valor é maior
# - não existe valor maior, os dois são iguais

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O primeiro valor é maior.")
elif numero2 > numero1:
    print("O segundo valor é maior.")
else:
    print("Não existe valor maior, os dois são iguais.")
