print('gerador de PA')
print('-='* 10)
pa = int(input('primeiro termo: '))
razao = int(input('razao da pa: '))
termo = pa
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end=' ')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('quantos termos você gostaria de ver a mais:'))
print('fim')