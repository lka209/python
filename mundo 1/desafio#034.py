s1 = float(input('qual é o salário do funcionário?R$'))
if s1 <= 702:
    n1 = s1 + (s1 * 10/100)
else:
    n1 = s1 + (s1 * 5/100)
    print('quem ganhava {:.2f} passa a ganhar R$ {:.2f}.'.format(s1, n1))