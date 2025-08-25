c = s = 0
while True:
    num = int(input('digite um numero[999 para parar]: '))
    if num == 999:
        break
    c += 1
    s += num
print(f'a soma dos {c} valores foi {s}')
