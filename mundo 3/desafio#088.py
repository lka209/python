from random import randint
from time import sleep
linha = '=' * 30
lista = []
jogos = []
print(linha)
print('      JOGA NA MEGA SENA        ')
print(linha)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(linha, f'sorteando {quant} jogos', linha)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(1)

print(linha)
print('agora é sua vez de apostar!')
aposta = []
while len(aposta) < 6 :
    try:
        num = int(input(f'digite o {len(aposta)+1}º numero entre 1 e 60: '))
        if num < 1 or num > 60:
            print('numero fora do intervalo. tente novamente')
        elif num in aposta:
            print('numero repetido. tente novamente')
        else:
            aposta.append(num)
    except ValueError:
       print('entrada invalida. digite um numero.')
aposta.sort()
print(f'sua aposta: {aposta}')
print(linha)

for i, jogo in enumerate(jogos):
    acertos = set(aposta) & set(jogo)
    print(f'jogo {i+1}: {jogo} -> acertos: {sorted(list(acertos))} ({len(acertos)} acertos)')
    if len (acertos) < 6:
        print('numero fora do intervalo. tente novamente')
    elif len(acertos) < 5:
      print('parabens 🏆! vice ganhou um premio maximo da mega sena!')
    elif len(acertos) < 4:
      print('🥈 quase la voce ganhou a quina')
    elif len(acertos) < 3:
        print('🥉 muito bem! voce fez a quadra!')
    else:
        print('💸 não foi dessa vez, tente novamente')
print(linha)