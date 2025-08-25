from time import sleep

linha = '-=' * 30

def contador(i, f, p):
    print(linha)
    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')
    sleep(0.25)

    if p == 0:
        p = 1

    if i < f:

        if p < 0:
            p = abs(p)
        for cont in range(i, f + 1, p):
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
    else:

        if p > 0:
            p = -p
        for cont in range(i, f - 1, p):
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)

    print('FIM')

# Testes automáticos
contador(1, 10, 1)
contador(10, 0, 2)

# Contagem personalizada pelo usuário
print(linha)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)
