# [10 / 100] Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1,00 = R$3,27

dinheiro_em_reais = float(input("Digite quantos reais você tem na carteira: "))
dinheiro_em_dolar = dinheiro_em_reais / 3.27
print(f"É possível comprar {dinheiro_em_dolar:.2f} dólares com R$ {dinheiro_em_reais:.2f}.")