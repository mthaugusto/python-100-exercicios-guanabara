# [11 / 100] Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2 m².

largura = float(input("Insira aqui a largura da parede: "))
altura = float(input("Insira aqui a altura da parede: "))
area = largura * altura
qtde_tinta = area / 2

print(f"A área da parede é: {area} m²")
print(f"Serão necessários {qtde_tinta} litros de tinta para pintar a parede.")