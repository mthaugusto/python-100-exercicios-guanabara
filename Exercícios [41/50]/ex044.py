# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal, e condição de pagamento:

# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - em 3x ou mais no cartão: 20% de juros

valor_produto = float(input("Insira o valor do produto: "))

print("Selecione a forma de pagamento:\n1 - À vista dinheiro/cheque (10% de desconto)\n2 - À vista no cartão (5% de desconto)\n3 - Em até 2x no cartão (preço normal)\n4 - Em 3x ou mais no cartão (20% de juros)\n")

opcao = int(input("Digite o número da opção desejada: "))

if opcao == 1:
    valor_final = valor_produto - (valor_produto * 0.1)
    print(f"Valor a ser pago: R$ {valor_final:.2f}")
elif opcao == 2:
    valor_final = valor_produto - (valor_produto * 0.05)
    print(f"Valor a ser pago: R$ {valor_final:.2f}")
elif opcao == 3:
    valor_final = valor_produto
    print(f"Valor a ser pago: R$ {valor_final:.2f}")
elif opcao == 4:
    parcelas = int(input("Digite o número de parcelas desejadas: "))
    if parcelas >= 3:
        valor_final = valor_produto + (valor_produto * 0.2)
        valor_parcela = valor_final / parcelas
        print(f"Valor a ser pago: R$ {valor_final:.2f}")
        print(f"Valor de cada parcela ({parcelas}x): R$ {valor_parcela:.2f}")
    else:
        print("Número de parcelas inválido.")
else:
    print("Opção inválida. Por favor, selecione uma opção válida.")
