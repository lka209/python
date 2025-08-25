resultado = ''.join(str(i) for i in range(30))
tamanho = len(resultado)

num = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Digite outro valor.')

    while True:
        r = input('Deseja continuar? [S/N] ').strip().upper()
        if r in ['S', 'N']:
            break
        else:
            print('Entrada inválida. Por favor, responda apenas com "S" ou "N".')
    if r == 'N':
        break
print('=' * tamanho)
num.sort()
print(f'Você digitou os números:{num}')
