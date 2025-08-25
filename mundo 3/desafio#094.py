galera = []
pessoas = {}
soma = media = 0
linha = '=' * 30
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F]: ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while (r := input('Deseja continuar? [S/N] ').strip().upper()) not in ['S', 'N']:
      print('Entrada inválida. Por favor, responda apenas com "S" ou "N".')
    if r == 'N':
          break
print(linha)
print(f'A) ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) a media de idade e de {media:5.2f} anos.')
print(f'C) as mulheres cadastradas foram', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'[{p["nome"]}] ', end='')
print()
print('D) lista das pessoas que estão acima da media: ')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('<< ENCERRADO >>')