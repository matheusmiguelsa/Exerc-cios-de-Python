a = int(input('Quantos dias alugados: '))
km = float(input('Quantos quilômetros rodados: '))
na = a*60
nkm = km*0.15
print('O total a pagar é de R${:.2f}'.format(na+nkm))