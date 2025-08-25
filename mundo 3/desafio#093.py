linha = '=' * 30
jogador  = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(linha)
print(jogador)
print(linha)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(linha)
print(f'o jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i}, fez {v} gols.')
print(f'foi um total de {jogador["total"]} gols.')
