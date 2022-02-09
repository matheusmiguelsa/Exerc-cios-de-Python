from math import sqrt, hypot
c = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = c**2+ca**2
# rh = sqrt(h)
# rh = h**(1/2)
rh = hypot(c, ca)
print('A hipotenusa vai medir {:.2f}'.format(rh))
