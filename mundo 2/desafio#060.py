#n = int(input('digite um numero para calcular seu fatorial: '))
#c = n
#f = 1
#print('calculando {}!'.format(n))
#while c > 0:
#    print('{}'.format(c), end='')
#    print(' x ' if c > 1 else ' = ', end='')
#    f *= c
#    c -= 1
#print('{}'.format(f))

n = int(input('digite um numero para calcular seu fatorial: '))
c = n
f = 1
print('calculando {}!'.format(n))
for c in range(n,0,-1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print('{}'.format(f))
