from random import randint
from time import sleep
p1 = (randint(0,20))

print('-=-'*20)
print('vou pensar em um numero entre 0 e 20, tente adivinhar'.format(p1))
print('-=-'*20)

j1 = int(input('em que numero eu pensei ? '))

print('processando...')
sleep(2)

if j1 == p1:
    print('parabéns, você ganhou!'.format(p1))
else:
    print('eu pensei no numero {}, não no número {}'.format(p1,j1))


