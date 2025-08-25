resultado = ''.join(str(i)for i in range(15))
tamanho = len(resultado)
while True:
     n = int(input('qual tabuada você gostaria de ver?'))
     print('=' * tamanho)
     if n < 0:
         break
     for c in range(1, 11):
         print(f'{n} x {c} = {n * c}')
     print('=' * tamanho)
print('fim do programa tabuada')