linha = '-=' * 30
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1': randint(1, 10),
        'jogador 2': randint(1, 10),
        'jogador 3': randint(1, 10),
        'jogador 4': randint(1, 10),}
ranking = {}
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking= sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(linha)
print('<<<<<RANKING DOS JOGADORES>>>>>:')
print(ranking)
for i, v in enumerate(ranking):
    print(f'({i+1})° lugar: {v[0]} com {v[1]}.')
    sleep(1)