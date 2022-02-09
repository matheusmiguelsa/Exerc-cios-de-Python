l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
ar = l*a
t = ar/2
print('Sua parede tem a dimensão {:.2f}mX{:.2f}m e sua área é de {:.2f}m² \nPara pintar essa parede, você precisaá de {:.2f} litros de tinta.'.format(l, a, ar, t))