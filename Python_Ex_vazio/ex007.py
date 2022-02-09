i = float(input('Digite a primeira nota do aluno: '))
ii = float(input('Digite a segunda nota do aluno: '))
riv = ('{}{}{}'.format('\033[31m', i, '\033[m'))
ria = ('{}{}{}'.format('\033[34m', i, '\033[m'))
riiv = ('{}{}{}'.format('\033[31m', ii, '\033[m'))
riia = ('{}{}{}'.format('\033[34m', ii, '\033[m'))
riiiv = ('{}{}{}'.format('\033[31m', (i+ii) / 2, '\033[m'))
riiia = ('{}{}{}'.format('\033[34m', (i+ii) / 2, '\033[m'))

if i >= 6:
    n1 = ria
else:
    n1 = riv
if ii >= 6:
    n2 = riia
else:
    n2 = riiv
if i + i >= 12:
    sn = riiia
else:
    sn = riiiv

print('A média entre {} e {} é {}'.format(n1, n2, sn))



