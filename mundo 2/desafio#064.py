num = cont = soma = 0
int(input('digite um numero [69 para parar]:'))
while num != 69:
    soma += num
    cont += 1
    num = int(input('digite um numero [69 para parar]:'))
print('voce digitou {} termos e a soma entre eles é {}'.format(cont, soma))