from datetime import date
atual = date.today().year
nascimento = int(input('digite seu ano de nascimento:'))
idade = atual - nascimento
print('o atleta tem {} anos'.format(idade))
if   idade <= 9:
    print(' categoria mirim')
elif idade <= 14:
    print('categoria infantil')
elif idade <= 19:
    print(' categoria junior ')
elif idade <= 25:
    print(' categoria sênior')
else:
    print(' categoria master')