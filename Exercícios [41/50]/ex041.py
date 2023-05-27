# A Confederação Nacional de Natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# - até 9 anos: mirim
# - até 14 anos: infantil
# - até 19 anos: júnior
# - até 20 anos: sênior
# acima de 20: master

from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input("Insira o ano de nascimento do atleta: "))

idade = ano_atual - ano_nascimento

if idade > 0 and idade <= 9:
    print("Categoria: mirim")

elif idade > 9 and idade <= 14:
    print("Categoria: infantil")

elif idade > 14 and idade <= 19:
    print("Categoria: júnior")

elif idade > 19 and idade <= 20:
    print("Categoria: sênior")

elif idade > 20:
    print("Categoria: master")

else: 
    print("Insira um ano de nascimento válido.")
