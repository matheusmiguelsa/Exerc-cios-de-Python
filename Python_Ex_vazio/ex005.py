i = int(input('Digite um número: '))
a = i-1
s = i+1
ri = ('{}{}{}'.format('\033[1;34;47m', i, '\033[m'))
ra = ('{}{}{}'.format('\033[1;34;43m', a, '\033[m'))
rs = ('{}{}{}'.format('\033[1;34;41m', s, '\033[m'))
x = ('O número que você digitou é {}, o antecessor é {} e o sucessor é {}'.format(ri, ra, rs))
print('{}'.format(x))
