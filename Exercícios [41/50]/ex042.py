# Refaça o DESAFIO 35, dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:

# - equilátero: todos os lados iguais
# - isósceles: dois lados iguais
# - escaleno: todos os lados diferentes

reta_a = float(input("Digite o comprimento A: "))
reta_b = float(input("Digite o comprimento B: "))
reta_c = float(input("Digite o comprimento C: "))

if reta_a + reta_b > reta_c and reta_a + reta_c > reta_b and reta_b + reta_c > reta_a:
    if reta_a == reta_b == reta_c:
        print("O triângulo pode ser formado e é um triângulo equilátero.")
    elif reta_a == reta_b or reta_a == reta_c or reta_b == reta_c:
        print("O triângulo pode ser formado e é um triângulo isósceles")
    else:
        print("O triângulo pode ser formado e é um triângulo escaleno.")

else:
    print("Não é possível formar um triângulo com essas medidas.")