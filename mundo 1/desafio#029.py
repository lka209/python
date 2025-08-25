v1 = float(input('qual a velocidade atual do seu carro?'))
if v1 > 80:
    print('MULTADO!, você está acima do limite de 80km/h na via.')
    multa = v1* 7
    print('você terá de pagar uma multa de R$ {:.2f}'.format(multa))
    print('dirija com segurança, have a lovely day Sr.')
