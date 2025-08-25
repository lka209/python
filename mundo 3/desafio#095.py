time = []
jogador = {}
partidas = []
linha = '-=' * 30

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break

print(linha)
print(f'{"Cod":<4}{"Nome":<15}{"Gols":<20}{"Total":<5}')
print(linha)
for i, jogador in enumerate(time):
    print(f'{i:<4}{jogador["nome"]:<15}{str(jogador["gols"]):<20}{jogador["total"]:<5}')
print(linha)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca < 0 or busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'   No jogo {i + 1} fez {g} gols.')
        print(linha)

print('<<< VOLTE SEMPRE >>>')
