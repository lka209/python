linha = '-=' * 30
aluno = dict ()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'RECUPERAÇÂO'
else:
    aluno['situacao'] = 'REPROVADO'
print(linha)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')