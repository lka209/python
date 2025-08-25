resultado = ''.join(str(i)for i in range(140))
tamanho = len(resultado)
times = ('Flamengo','Cruzeiro','Palmeiras','Bahia','Mirassol','Bragantino',
        'Botafogo','São Paulo','Fluminense','Atlético-MG','Ceará SC','Corinthians',
        'Internacional','Grêmio','EC Vitória','Vasco da Gama','Santos','Fortaleza',
        'Juventude','Sport Recife')
print('=' * tamanho)
print(f'Os 5 primeiros times são {times[0:5]}')
print('=' * tamanho)
print(f'Os 4 ultimos colocados são {times[-4:]}')
print('=' * tamanho)
print(f'A ordem alfabética fica da seguinte forma:{sorted(times)}')
print('=' * tamanho)
print(f'O Botafogo está na posição: {times.index('Botafogo')}')
print('=' * tamanho)