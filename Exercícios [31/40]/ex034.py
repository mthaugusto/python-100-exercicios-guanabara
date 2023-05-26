# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1250.00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é 15%.

salario = float(input("Digite o salário do funcionário: "))

if salario > 1250:
    salario_aumento = salario + (salario * 0.10)

else:
    salario_aumento = salario + (salario * 0.15)

print(f"O novo salário do funcionário será de: {salario_aumento}")