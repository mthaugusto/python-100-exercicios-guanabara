# [9 / 100] Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input("Insira um número inteiro: "))
print(f'{num} x 1 = {num*1}')
print(f'{num} x 2 = {num*2}')
print(f'{num} x 3 = {num*3}')
print(f'{num} x 4 = {num*4}')
print(f'{num} x 5 = {num*5}')
print(f'{num} x 6 = {num*6}')
print(f'{num} x 7 = {num*7}')
print(f'{num} x 8 = {num*8}')
print(f'{num} x 9 = {num*9}')
print(f'{num} x 10 = {num*10}')

# -----------------------------

# Ainda estamos no início do curso, mas claro que a melhor maneira seria usar uma estrutura de repetição, como por exemplo:

# num = int(input("Insira um número inteiro: "))
# contador = 1
# for i in range (10):
#     print(f"{num} x {contador} = {num*contador}")
#     contador += 1