# [17 / 100] Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

# Vale lembrar que o cálculo da hipotenusa é enunciado pelo Teorema de Pitágoras, que diz: “A hipotenusa é igual à raiz quadrada da soma dos catetos ao quadrado”.

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = ((cateto_oposto ** 2) + (cateto_adjacente ** 2)) ** 0.5

print(f"O comprimento da hipotenusa é: {hipotenusa}")
