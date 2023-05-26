# [6 / 100] Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input("Insira aqui um número: "))
num_dobro = num * 2
num_triplo = num * 3
num_raiz = num ** 1/2

print(f"O dobro de {num} é: {num_dobro}\nO triplo de {num} é: {num_triplo}\nA raíz de {num} é: {num_raiz.:2f}")