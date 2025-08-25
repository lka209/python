listagem = ('caderno', 10.90,
            'borracha', 2.00,
            'lápis', 1.50,
            'corretivo', 4.50,
            'mochila', 120.00,
            'lapiseira', 5.00)
print('=' * 40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('=' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('='* 40)