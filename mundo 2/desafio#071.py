resultado = ''.join(str(i)for i in range(20))
tamanho = len(resultado)
print('=' * tamanho)
print('{:-^30}'.format('BANCO DO XINON!'))
print('=' * tamanho)
valor = int(input('qual valor voce quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'total de {totced} cedulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * tamanho)
print('{:-^30}'.format('volte sempre ao BANCO DO XINON!, have a great day!'))

