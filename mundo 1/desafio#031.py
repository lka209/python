d1 = float(input('Digite a distância em KM do ponto A ao ponto B: '))
print('Você está prestes a fazer uma viagem de {:.2f} KM.'.format(d1))
p1_a1 = d1 * 3.5 if d1 <= 400 else d1 * 4.0
p1_c1 = d1 * 1.5 if d1 <= 200 else d1 * 3.5
print('Do ponto A ao ponto B, a passagem de carro custará R$ {:.2f}.'.format(p1_c1))
print('Se for de avião, você pagará o valor de R$ {:.2f}.'.format(p1_a1))