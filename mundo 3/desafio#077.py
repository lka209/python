palavras = ('trabalhar','curso','estudar','mercado','praticar')
for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')