# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0.50 por km para viagens de até 200km e R$ 0.45 para viagens mais longas.

distancia = float(input("Digite a distância de uma viagem em km: "))

if distancia <= 200:
    valor_total = distancia * 0.5

else:
    valor_total = distancia * 0.45

print(f"O valor total da passagem é de: {valor_total}")