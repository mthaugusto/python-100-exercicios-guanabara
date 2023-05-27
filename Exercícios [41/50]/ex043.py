# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
# e mostre seu status, e acordo com a tabela abaixo:

# - abaixo de 18.5: abaixo do peso
# - entre 18.5 e 25: peso ideal
# - 25 até 30: sobrepeso
# - 30 até 40: obesidade
# - acima de 40: obesidade mórbida

peso = float(input("Insira o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = (peso / (altura * altura))

if imc < 18.5:
    print("Você está abaixo do peso")
elif imc >= 18.5 and imc <= 25:
    print("Você está no seu peso ideal")
elif imc > 25 and imc <= 30:
    print("Você está no sobrepeso")
elif imc > 30 and imc <= 40:
    print("Você está na obesidade")
else:
    print("Você está na obesidade mórbida")
