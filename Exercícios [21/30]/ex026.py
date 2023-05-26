# [26 / 100] Faça um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez, em que posição ela aparece a última vez.

frase = input("Insira uma frase: ").lower()
contador_a = 0

# Número total usando for
for x in frase:
    if x == 'a':
        contador_a += 1

print(f"O número total de 'A' na frase é: {contador_a}")

# Número total usando a função count()

total_a = frase.count('a')
print(f"O número total de 'A' na frase é: {total_a}")

# Posição em que aparece a primeira vez usando for

for i in range(len(frase)):
    if frase[i] == 'a':
        index_a = i
        break

print(f"O primeiro 'A' aparece na posição {index_a}")

# Posição em que aparece a primeira vez usando a função find()

primeira_a = frase.find("a")

print(f"O primeiro 'A' aparece na posição {primeira_a}")

# Posição em que aparece a última vez usando for

for i in range(len(frase)-1, -1, -1):
    if frase[i] == 'a':
        last_index_a = i
        break

print(f"O ultimo 'A' aparece na posição {last_index_a}")

# Posição em que aparece a última vez usando a função rfind()

ultimo_a = frase.rfind("a")

print(f"O ultimo 'A' aparece na posição {ultimo_a}")
