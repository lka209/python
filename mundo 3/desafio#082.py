resultado = ''.join(str(i)for i in range(20))
tamanho = len(resultado)
num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um valor: ')))
    while True:
        resp = input('Deseja continuar? [S/N] ').strip().upper()
        if resp in ['S', 'N']:
            break
        else:
            print('Entrada inválida. Por favor, responda apenas com "S" ou "N".')
    if resp == 'N':
         break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('=' * tamanho)
print(f'a lista completa é {num}')
print(f'a lista de pares é {pares}')
print(f'a lista de impares é {impares}')