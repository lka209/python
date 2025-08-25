from datetime import datetime
linha = '-=' * 30
dados = dict()
dados['nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento

ctps = int(input('Carteira de trabalho (0 se não tem): '))
if ctps != 0:
    dados['ctps'] = ctps
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35 - datetime.now().year)
print(linha)
print('\nDados cadastrados:')
for chave, valor in dados.items():
    print(f'  {chave.capitalize()}: {valor}')
