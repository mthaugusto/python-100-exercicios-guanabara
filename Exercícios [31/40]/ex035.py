# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

reta_a = float(input("Digite o comprimento A: "))
reta_b = float(input("Digite o comprimento B: "))
reta_c = float(input("Digite o comprimento C: "))

if reta_a + reta_b > reta_c and reta_a + reta_c > reta_b and reta_b + reta_c > reta_a:
    print("O triângulo pode ser formado.")

else:
    print("Não é possível formar um triângulo com essas medidas.")
