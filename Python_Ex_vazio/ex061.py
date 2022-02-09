pt = int(input('Digite o primeiro termo de uma PA: '))
rz = int(input('Digite a razão de uma PA: '))
ut = pt + rz * (10 - 1)
pt2 = pt
cont = 1
while cont <= 10:#errei colocando while p2 < ut
    print(pt2, end = ' -> ')
    pt2 += rz
    cont += 1
print('Acabou')