# [13 / 100] Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Insira o salário do funcionário: "))
salario_aumento = salario + (salario * 0.15)

print(f'O novo salário do funcionário, com 15% de aumento é de: R${salario_aumento}')