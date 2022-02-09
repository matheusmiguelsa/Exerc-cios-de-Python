
pt = int(input('Digite o primeiro termo de uma PA: '))
rz = int(input('Digite a razão de uma PA: '))
ut = pt + rz * (10 - 1)
pt2 = pt
cont = 1
total = 0
mais = 10
continuar =''

while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(pt2), end = '')
        pt2 += rz
        cont += 1
    print('FIM')
    mais = int(input('\nDeseja ver mais quantos termos? '))

print('Acabou')




