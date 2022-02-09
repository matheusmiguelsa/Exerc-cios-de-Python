pt = int(input('Digite o primeiro termo de uma PA: '))
rz = int(input('Digite a razão de uma PA: '))
ut = pt + rz * (10 - 1)
for c in range(pt, ut + 1, rz):
    print(c, end = ' -> ')
print('Acabou')