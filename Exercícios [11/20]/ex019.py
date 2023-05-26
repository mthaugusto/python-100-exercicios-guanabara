# [19 / 100] Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

alunos = [aluno1, aluno2, aluno3, aluno4]

escolha_aleatoria = random.randint(0, 3) # Irá sortear um número entre 0, 1, 2 e 3

aluno_escolhido = alunos[escolha_aleatoria] # Irá acessar a lista alunos, com um dos quatro números sorteados como index.

print(f"O aluno escolhido para apagar o quadro foi: {aluno_escolhido}")

# --------------------------------------------------

#Poderíamos também usar a função choice da biblioteca random, que escolhe uma opção entre uma lista específica de elementos. Por ex:

# aluno1 = input("Digite o nome do primeiro aluno: ")
# aluno2 = input("Digite o nome do segundo aluno: ")
# aluno3 = input("Digite o nome do terceiro aluno: ")
# aluno4 = input("Digite o nome do quarto aluno: ")

# alunos = [aluno1, aluno2, aluno3, aluno4]

# escolha_aleatoria = random.choice(alunos)

# print(f"O aluno escolhido para apagar o quadro foi: {escolha_aleatoria}"")
