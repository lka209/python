num = int(input('digite um numero inteiro:'))
print('''escolha uma das bases para conversão:
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('sua opção:'))
if opcao == 1:
    print('{} convertido para binário e igual a {}'.format(opcao, bin(num)[2:]))
elif opcao == 2:
 print('{} convertido para octal e igual a {}'.format(opcao, oct(num)[2:]))
elif opcao == 3:
 print('{} convertido para hexadecimal e igual a {}'.format(opcao, hex(num)[2:]))
else:
    print('opção invalida, tente novamente mais tarde.')