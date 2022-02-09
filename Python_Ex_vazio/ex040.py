n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota'))
media =('{}{}'.format('\033[31m', n1 + n2))
print('Tirando {} e {}, a média é {}'.format(n1, n2, (n1 +n2) / 2))
if (n1 + n2) / 2 < 5:
    print('{}Reprovado'.format('\033[31m'))
elif (n1 + n2) / 2 >= 5 and (n1 + n2) / 2 < 7:
    print('{}Recuperação'.format('\033[33m'))
else:
    print('{}Aprovado'.format('\033[34m'))