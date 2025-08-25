maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
            if peso < menor:
                menor = peso
print('maior peso lido foi {} KG'.format(maior))
print('menor peso lido foi {} KG'.format(menor))