from datetime import date
a1 = int(input('Qual ano você gostaria de analisar?'))
if a1 == 0:
    a1 = date.today().year
if a1 % 4 == 0 and a1 % 100 != 0 or a1 % 400 == 0:
    print('o ano {} é BISSEXTO'.format(a1))
else:
    print('o ano {} não é BISSEXTO'.format(a1))
