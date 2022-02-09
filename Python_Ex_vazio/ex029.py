n1 = float(input('Velocidade do carro: '))
n2 = (n1-80)*7
if n1 <= 80:
    print('Siga sem ser multado!')
elif n1 > 80:
    print('Imprudente! Sera multado em R${:.2f}!'.format(n2))
if n1 > 200:
    print('Sua vida vale tão pouco assim??')
