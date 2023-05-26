# [15 / 100] Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km_percorridos = float(input("Insira o total de quilômetros percorridos: "))
dias_alugado = int(input("Por quantos dias o carro ficou alugado: "))

preco_dias_alugado = dias_alugado * 60
preco_km_percorridos = km_percorridos * 0.15
preco_total = preco_dias_alugado + preco_km_percorridos

print(f"O valor total a ser pago é de R$ {preco_total:.2f}.")