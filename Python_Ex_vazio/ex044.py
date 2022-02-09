print('{:=^40}'.format(' LOJAS SÁ '))
print('1: dinheiro\n2: cheque\n3: cartão')
i = int(input('Digite a forma de pagamento: '))
v = float(input('Digite o valor do produto: R$'))
if i == 3:
    a = int(input('Digite em quantas vezes no cartão: '))
    if a == 1:
        print('O valor a ser pago em uma vez no cartão é de R${:.2f}'.format(v * 0.95))
    elif a == 2:
        print('O valor a ser pago em duas vezes no cartão é de R${:.2f}, cada parcela será de R${:.2f}'.format(v, v / 2))
    elif a == 3:
        print('O valor a ser pago em três vezes no cartão é de R${:.2f}, cada parcela será de R${:.2f}'.format(v * 1.2, (v * 1.2) / 3))
else:
    if i == 1:
        print('O valor a ser pago em dinheiro é de R${:.2f}'.format(v * 0.9))
    elif i == 2:
        print('O valor a ser pago com cheque é de R${:.2f}'.format(v * 0.9))
