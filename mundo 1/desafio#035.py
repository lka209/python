print ('-=-'*10)
print ('analisar de triangulos')
print('-=-'*10)
r1, r2, r3 = 0, 0, 0
float(input('primeiro segmento:'))
float(input('segundo segmento:'))
float(input('terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acima podem formar um triangulo')
else:
    print('os segmentos acima não formam um triangulo')