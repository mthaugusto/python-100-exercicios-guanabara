# [22 / 100] Crie um programa que leia o nome completo de uma pessoa e mostre o nome com todas as letras maiúsculas, com todas as minúsculas, quantas letras ao todo (sem contar os espaços) e quantas letras tem o primeiro nome.

nome = input("Insira aqui o seu nome completo: ")

nome_maiusculo = nome.upper() # Converter para maiúsculas

nome_minusculo = nome.lower() # Converter para minúsculas

total_letras = len(nome.replace(" ", "")) # Aqui estamos usando o método replace para substituir o caractere barra de espaço (" ") por nenhum caractere ("") e posteriormente a função len () para contar quantos caracteres temos.


nome_dividido = nome.split() # Divide o nome pelos espaços e retorna o mesmo no formato de uma lista ex: ['Matheus', 'Leite'] 

primeiro_nome = nome_dividido[0] # Usando o índice 0 para localizar qual o primeiro nome na lista criada anteriormente

tamanho_primeiro_nome = len(primeiro_nome) # Contabiliza o tamanho do primeiro nome


print(f"Nome com letras maiúsculas: {nome_maiusculo}")
print(f"Nome com letras minúsculas: {nome_minusculo}")
print(f"Quantidade total de letras: {total_letras}")
print(f"Quantidade de letras do primeiro nome: {tamanho_primeiro_nome}")


