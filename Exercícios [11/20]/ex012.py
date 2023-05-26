# [12 / 100] Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Insira o preço do produto: "))
preco_desconto = preco - (preco * 0.05)

print(f'O valor do produto com desconto de 5% é R${preco_desconto:.2f}.')