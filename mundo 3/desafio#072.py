cont = ('zero','um','dois','tres','quatro','cinco','seis',
        'sete','oito','nove','dez','onze','doze','treze',
        'quatorze','quinze','dezesseis','dezessete','dezoito',
        'dezenove','vinte')
while True:
    num = int(input('digite um numero de 0 a 20: '))
    if 0 <= num <= 20:
     print(f'voce digitou o numero: {cont[num]}')
    else:
     print('numero fora do intervalo, tente novamente ', end='')
    continuar = input('quer continuar? [s/n] ').strip().lower()[0]
    if continuar.startswith('n'):
       print('encerrando o programa...')
       break