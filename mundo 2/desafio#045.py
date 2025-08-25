import random

opcoes = ['pedra', 'papel', 'tesoura', 'lagarto', 'spock']

regras = {
    "tesoura": ["papel", "lagarto"],
    "papel": ["pedra", "spock"],
    "pedra": ["lagarto", "tesoura"],
    "lagarto": ["spock", "papel"],
    "spock": ["tesoura", "pedra"]
    }

def resultado(jogador, computador):
    if jogador == computador:
        return "Empate!"
    elif computador in regras[jogador]:
        return "Você venceu!"
    else:
        return "Você perdeu!"

while True:
    print("\nEscolha: pedra, papel, tesoura, lagarto ou spock (ou 'sair' para encerrar)")
    jogador = input("Sua escolha: ").lower()

    if jogador == 'sair':
        print('Obrigado por jogar!')
        break

    if jogador not in opcoes:
        print("Escolha inválida. Tente novamente.")
        continue

    computador = random.choice(opcoes)
    print(f'Computador escolheu: {computador}')
    print(resultado(jogador, computador))


