r1 = float(input('Digite o tamanho da primeira reta em centímetros: '))
r2 = float(input('Digite o tamanho da segunda reta em centímetros: '))
r3 = float(input('Digite o tamanho da terceira reta em centímetros: '))
maior = r1
if r2 > r1 and r2 > r3:
    maior = r2
if r3 > r1 and r3 > r2:
    maior = r3
menor = r1
if r2 < r1 and r2 < r3:
    menor = r2
if r3 < r1 and r3 < r2:
    menor = r3
medio = r1
if r1 < r2 < r3 or r3 < r2 < r1:
    medio = r2
if r1 < r3 < r2 or r2 < r3 < r1:
    medio = r3
r4 = (medio + menor) - maior
if r4 > 0:
    print('É possível que as 3 retas formem um triângulo, \n sendo a maior reta {}cm, a média {}cm e a menor {}cm'.format(maior, medio, menor))
if r4 <= 0:
    print('Não é possível que as 3 retas formem um triângulo, \n sendo a maior reta {}cm, a média {}cm e a menor {}cm'.format(maior, medio, menor))
print('Simulação da proporção das retas em centímetros inteiros: ')
n1 = r1
n2 = r2
n3 = r3
print('_' * (int(maior)))
print('_' * (int(medio)))
print('_' * (int(menor)))
if maior == medio == menor and r4 > 0:
    print('É um triângulo equilátero')
if r4 > 0 and maior == medio != menor or medio == menor != maior and r4 > 0:
    print('É um triângulo isóceles')
if maior != medio != menor and r4 > 0:
    print('É um triângulo escaleno')


