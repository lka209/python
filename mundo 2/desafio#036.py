C1 = int(input('Digite o valor do lote:R$'))
S1 = int(input('Quanto é o seu salário?:R$'))
T1 = int(input('quanto tempo de financiamento?'))
F1 = C1 / (T1 * 12)
M1 = S1 * 30/100
print('para pagar um lote de {}R$, em {} anos'.format(C1, T1, end =''))
print('a prestação será de {}R$.'.format(F1))
if F1 <= M1:
    print('Financiamento aprovado com sucesso.')
else:
    print('Financiamento negado.')