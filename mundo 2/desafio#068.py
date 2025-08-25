v = 0
from random import randint
while True:
    jogador = int(input('digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('par ou impar ?[P/I] ')).strip().upper()[0]
    print(f'voce jogou {jogador} e o computador {computador}. total de {total}')
    print('deu par' if total % 2 == 0 else 'deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('voce venceu')
            v += 1
        else:
            print('voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
             print('voce venceu')
             v += 1
        else:
            print('voce perdeu')
            break
    print('vamos jogar novamente')
print(f'GAME OVER! voce venceu {v} vezes')
