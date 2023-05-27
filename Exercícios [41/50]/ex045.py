# Crie um programa que faça o computador jogar Jokenpô com você.
import random

jokenpo = ['pedra', 'papel', 'tesoura']
indice_aleatorio = random.randint(0, 2)
escolha_pc = jokenpo[indice_aleatorio]

escolha_usuario = input("Digite uma das opções - pedra/papel/tesoura: ").lower()

print(f"A escolha do computador foi: {escolha_pc}")

if escolha_pc == escolha_usuario:
    print("Empate")
    
elif escolha_usuario == 'pedra':
    if escolha_pc == 'papel':
        print("Você perdeu! Papel embrulha pedra.")
    else:
        print("Você ganhou! Pedra quebra tesoura.")
        
elif escolha_usuario == 'papel':
    if escolha_pc == 'tesoura':
        print("Você perdeu! Tesoura corta papel.")
    else:
        print("Você ganhou! Papel embrulha pedra.")
        
elif escolha_usuario == 'tesoura':
    if escolha_pc == 'pedra':
        print("Você perdeu! Pedra quebra tesoura.")
    else:
        print("Você ganhou! Tesoura corta papel.")
        
else:
    print("Opção inválida. Por favor, escolha entre pedra, papel ou tesoura.")
