somaidade = 0
maioridadedehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print('-------- {}ª PESSOA --------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip().upper()

    somaidade += idade

    if sexo == 'M':
        if idade > maioridadedehomem:
            maioridadedehomem = idade
            nomevelho = nome

    if sexo == 'F' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4

print('A média de idade do grupo é de {:.1f} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadedehomem, nomevelho if nomevelho else 'N/A'))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))
