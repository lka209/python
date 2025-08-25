preco = float(input('Digite o valor da compra: R$ '))

print('\nFormas de pagamento:')
print('[1] Pix')
print('[2] Dinheiro')
print('[3] Cartão de crédito')
print('[4] Cartão de débito')

print('=' * 40)
opcao = int(input('Escolha a opção de pagamento: '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('\nPagamento via Pix selecionado.')
    print(f'Desconto de 10% aplicado. Valor final: R$ {total:.2f}')

elif opcao == 2:
    total = preco - (preco * 15 / 100)
    print('\nPagamento em dinheiro selecionado.')
    print(f'Valor final: R$ {total:.2f} ')

elif opcao == 3:
    print('\nPagamento com cartão de crédito selecionado.')
    parcelas = int(input('Quantas parcelas? '))

    if parcelas == 1:
        total = preco - (preco * 5 / 100)
        print('Desconto de 5% aplicado para pagamento à vista no crédito.')
    elif parcelas > 1:
        total = preco
        print(f'Sem desconto para parcelamento em {parcelas}x.')

    valor_parcela = total / parcelas
    print(f'Você pagará {parcelas}x de R$ {valor_parcela:.2f}.')
    print(f'Valor total: R$ {total:.2f}')

elif opcao == 4:
    total = preco
    print('\nPagamento com cartão de débito selecionado.')
    print(f'Valor total: R$ {total:.2f} (sem desconto)')

else:
    print('\nOpção inválida. Tente novamente.')
    total = 0
