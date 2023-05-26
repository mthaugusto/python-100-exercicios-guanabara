# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base da conversão:
# 1 - para binário
# 2 - para octal 
# 3 - para hexadecimal

numero = int(input("Digite um número inteiro: "))
opcao = int(input("Escolha a base de conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n"))

# USAMOS AS FUNÇOES BIN(), OCT() E HEX()

if opcao == 1:
    resultado = bin(numero)
    print(f"O número {numero} convertido para binário é: {resultado}")
elif opcao == 2:
    resultado = oct(numero)
    print(f"O número {numero} convertido para octal é: {resultado}")
elif opcao == 3:
    resultado = hex(numero)
    print(f"O número {numero} convertido para hexadecimal é: {resultado}")
else:
    print("Opção inválida. Escolha uma opção entre 1, 2 e 3.")
