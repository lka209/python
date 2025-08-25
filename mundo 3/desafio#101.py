def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        return f'com {idade} anos: nao vota'
    elif idade == 18:
        return f'com {idade} anos: opcional'
    else:
        return f'com {idade} anos: obrigatorio'

nasc = int(input('ano em que nasceu: '))
print(voto(nasc))