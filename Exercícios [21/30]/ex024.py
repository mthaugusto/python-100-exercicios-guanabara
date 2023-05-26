# [24 / 100] Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input("Insira o nome de uma cidade: ").upper()

if cidade.startswith('SANTO'):
    print("A cidade começa com 'Santo'")

else:
    print("A cidade não começa com 'Santo'")