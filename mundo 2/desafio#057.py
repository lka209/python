sexo = str(input('informe seu sexo [M/F]:')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('ERROR. Por favor apenas digite M ou F ')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sexo))


