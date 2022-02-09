v = float(input('Valor da casa a ser comprada: R$'))
s = float(input('Salário do comprador: R$'))
qa = float(input('Quantos anos irá pagar: '))
print('Para pagar uma casa de R${:.2f} em {:.0f} anos'.format(v, qa), end='')
print(' a prestação sera de R${:.2f}'.format(v / (qa * 12)))

if v / (qa* 12) >= s * 0.3:
    print('Seu empréstimo foi negado, sinto muito')
else:
    print('Seu empréstimo foi aprovado, parabéns!!')