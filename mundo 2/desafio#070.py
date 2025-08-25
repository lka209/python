total = totalmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('nome do produto: '))
    preco = float(input('preço : R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totalmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resp in 'N':
            break
    print('{:-^40}'.format('fim do programa'))
    print(f'O total da compra foi R${total:.2f}')
    print(f'Temos {totalmil} produtos custando mais de R$1000.00')
    print(f'o produto mais barato foi {barato} que custa R${menor:.2f}')