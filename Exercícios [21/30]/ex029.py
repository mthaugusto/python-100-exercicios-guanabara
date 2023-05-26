# [29 / 100] Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7.00 por cada Km acima do limite.

velocidade = float(input("Insira a velocidade do carro: "))

if velocidade <= 80:
    print("A velocidade do motorista estava dentro dos limites")
else:
    velocidade_excedente = velocidade - 80
    multa = velocidade_excedente * 7
    print(f"O valor da multa é de R$ {multa:.2f}")

