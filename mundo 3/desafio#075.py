num = (int(input('digite um numero')),
       int(input('digite mais um numero')),
       int(input('digite outro numero')),
       int(input('digite o ultimo numero')))
print(f'voce digitou os valores {num}')
print(f'o valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print('o valor 3 não foi digitado na {num.index(3)+1}ª em nenhuma posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
