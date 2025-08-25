tot18 = totH = totM20 = 0
while True:
    idade = int(input('digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('digite seu sexo (M/F): ')).upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F':
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
    print(f'total de pessoas com ou mais de 18 anos: {tot18}')
    print(f'ao todos temos {totH} homens cadastrados')
    print(f'e temos {totM20} menos de 20 anos')