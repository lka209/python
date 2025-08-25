lin = '-=' * 20

def area (larg, comp):
    a = larg * comp
    print(f'a area de um terreno {larg} x {comp} é de {a}m²')

print(lin)
print('CONTROLE DE TERRENOS'.center(40))
print(lin)
l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
area(l, c)