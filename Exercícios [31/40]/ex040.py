# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida

# - Média abaixo de 5: reprovado
# - Média entre 5 e 6.9: recuperação
# - Média 7.0 ou superior: aprovado

nota1 = float(input("Insira aqui a Nota 1: "))
nota2 = float(input("Insira aqui a Nota 2: "))
media = (nota1 + nota2) / 2

if media < 5:
    print("REPROVADO!")
elif media >= 5 and media < 7:
    print("Você está de recuperação")
elif media >= 7 and media <= 10:
    print("APROVADO!")
else: 
    print("Você digitou algum valor inválido")
