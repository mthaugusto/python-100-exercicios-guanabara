# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Insira o valor total do imóvel: "))
salario = float(input("Insira o seu salário: "))
prazo_financiamento = int(input("Insira em quantos anos você deseja pagar: "))

prazo_financiamento_em_meses = prazo_financiamento * 12
prestacao_mensal = valor_casa / prazo_financiamento_em_meses
salario_trinta_porcento = salario * 30/100

if prestacao_mensal > salario_trinta_porcento:
    print("Empréstimo negado. O valor da prestação não pode exceder 30% de seu salário")

else:
    print("Empréstimo aprovado")