from math import sqrt
i = int(input('Digite um número: '))
d = i*2
t = i*3
r = sqrt(i)
x = ('{}O dobro de {} vale {}\nO triplo de {} vale {}\nA raiz quadrada de {} é igual a {:.2f}'.format('\033[34m', i, d, i, t, i, r, '\033[m'))
print(x)