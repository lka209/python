from datetime import date
atual = date.today().year
nascimento = int(input('ano de nascimento: '))
idade = atual - nascimento
print('quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade == 18:
    print('voce tem que se alistar de imediato')
elif idade < 18:
    saldo = 18 - idade
    print('ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('seu alistamento sera em {}'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('voce deveria ter ser alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('seu alistamento foi em {}'.format(ano))
  