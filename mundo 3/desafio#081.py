resultado = ''.join(str(i)for i in range(30))
tamanho = len(resultado)
val = []
while True:
    val.append(int(input('Digite um valor: ')))
    while True:
        resp = input('Deseja continuar? [S/N] ').strip().upper()
        if resp in ['S', 'N']:
            break
        else:
            print('Entrada inválida. Por favor, responda apenas com "S" ou "N".')
    if resp == 'N':
         break

print('=' * tamanho)
print(f'voce digitou {len(val)} elementos')
val.sort(reverse=True)
print(f'os valores em ordem decrescente são {val}')
if 5 in val:
    print('o valor 5 esta na lista')
else:
    print('o valor 5 não foi encontrado na lista')
