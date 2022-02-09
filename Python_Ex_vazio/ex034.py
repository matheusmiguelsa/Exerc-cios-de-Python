n1 = float(input('Digite seu salário para calcular seu aumento: R$'))
if n1 > 1250.00:
    n2 = n1*1.10
else:
    n2 = n1*1.15
if n1 > 1250.00:
    n3 = '10%'
else:
    n3 = '15%'
print('O aumento recebido foi de R${}, totalizando R${:.2f}'.format(n3, n2))
