# Refaça o exerrcício 009 (tabuada), mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

numero = int(input("Insira um número: "))

for x in range(1, 11):
    print(f"{numero} x {x} = {numero * x}")