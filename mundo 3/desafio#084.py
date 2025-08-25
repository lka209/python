linha = '=' * 45
pessoas = []
maior = menor = 0

while True:
    nome = input('Nome: ')
    peso = int(input('Peso: '))
    pessoas.append([nome, peso])

    if len(pessoas) == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    while True:
        r = input('Deseja continuar? [S/N]: ').strip().upper()
        if r in ['S', 'N']:
            break
        else:
            print('Entrada inválida. Por favor, responda apenas com "S" ou "N".')

    if r == 'N':
        break

print(linha)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior} Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor} Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()



