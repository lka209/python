resultado = ''.join(str(i)for i in range(220))
tamanho = len(resultado)
print('=' * 22)
print('sequência de Fibonacci')
print('=' * 22)
n = int(input('quantos termos você quer mostrar?'))
t1 = 0
t2 = 1
print('=' * tamanho)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('-> fim')
print('=' * tamanho)