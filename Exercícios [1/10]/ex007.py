# [7 / 100] Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome_aluno = input("Digite o nome do aluno: ")
nota_1 = float(input("Insira a nota da prova1: "))
nota_2 = float(input("Insira a nota da prova2: "))
media = (nota_1+nota_2)/2

print(f"A média de notas do aluno {nome_aluno} é: {media:.2f}")