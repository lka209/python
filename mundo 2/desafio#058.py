from random import randint
p1 = (randint(0,10))

print('-=-'*22)
print('''sou seu computador...acabei de pensar em um numero entre 0 e 10? 
sera que voce consegue adivinhar qual numero eu pensei?''')
print('-=-'*22)
acertou = False
palpites = 0
while not acertou:
    j1 = int(input('Em que numero eu pensei ? '))
    palpites += 1
    if j1 == p1:
      acertou = True
    else:
        if j1 < p1:
            print('errou esta perto')
        elif j1 > p1:
            print('errou mas esta longe')
print('acertou com {} palpites'.format(palpites))

