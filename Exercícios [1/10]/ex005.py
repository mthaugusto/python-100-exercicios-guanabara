# [5 / 100] Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num_inteiro = int(input("Insira um número inteiro: "))
num_inteiro_antecessor = num_inteiro - 1
num_inteiro_sucessor = num_inteiro + 1

print(f"O antecessor do número {num_inteiro} é {num_inteiro_antecessor} e o seu sucessor é {num_inteiro_sucessor}.")