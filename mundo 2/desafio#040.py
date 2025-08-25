nota1 = float(input('nota 1: '))
nota2 = float(input('nota 2: '))
media = (nota1 + nota2)/2
print('tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1,nota2,media))
if 7 > media >= 5:
    print('o aluno esta em recuperação')
elif media < 5:
    print('o aluno esta reprovado')
elif media >= 7:
    print('o aluno esta aprovado')