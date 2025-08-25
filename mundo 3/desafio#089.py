ficha = []
linha = '-=' * 30
while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    while (r := input('Deseja continuar? [S/N] ').strip().upper()) not in ['S', 'N']:
        print('Entrada inválida. Por favor, responda apenas com "S" ou "N".')
    if r == 'N':
        break
print(linha)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print(linha)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print(linha)
    opc = int(input('mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('fim')
        break
    if opc <= len(ficha) - 1:
        print(f'notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')