from time import sleep

linha = '-=' * 30


def maior(*num):
    print(linha)
    print('\nAnalisando os valores passados...')

    if len(num) == 0:
        print('Nenhum valor foi informado.')
        print('Não há maior valor.')
        return

    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)

    print(f'\nForam informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}')



maior(2, 3, 4, 5, 6, 7, 8, 9)
maior(2, 3, 4, 5, 6, 7)
maior(1, 2)
maior(6)
maior()
