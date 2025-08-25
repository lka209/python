frase = str(input('Digite uma frase: '))
palavras = frase.split()
junto = ' '.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print('temos um palindromo!')
else:
    print('a frase digitada não é um palindromo!')
