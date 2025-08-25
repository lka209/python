n1=int(input('digite um numero:'))
n2=int(input('digite outro numero:'))
d=n1/n2
s=n1+n2
m=n1-n2
di=n1//n2
e=n1**n2
print('a soma é {},o produto é {},a divisão é {:.2f}'.format(s,m,d), end=' ')
print('Divisão inteira {:.2f},potência inteira {:0f}'.format(di,e))
