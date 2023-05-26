# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - se ele ainda vai se alistar ao serviço militar
# - se é hora de se alistar
# - se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

# Importamos a biblioteca datetime para usarmos a função date e descobrirmos o ano atual, porém poderíamos usar a variável ano_atual com 2023 atribuido a ela, claro

ano_atual = date.today().year
ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = ano_atual - ano_nascimento

if idade < 18:
    anos_restantes = 18 - idade
    print("Você ainda vai se alistar ao serviço militar.")
    print(f"Faltam {anos_restantes} anos para o seu alistamento.")
elif idade == 18:
    print("É hora de se alistar ao serviço militar!")
else:
    anos_passados = idade - 18
    print("Já passou do tempo do alistamento.")
    print(f"Você está {anos_passados} anos atrasado(a) com o alistamento.")
