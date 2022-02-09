n1 = str(input('Digite uma frase: ').strip())
n2 = n1.lower()
nx = n2.split()
ny = ''.join(nx)
n3 = n2.count('a')
n4 = ny.find('a') + 1
n5 = ny.rfind('a') + 1
print('A letra A aparece {} vezes na frase.\nA primeira letra A apareceu na posição {}\nA última letra A apareceu na posição {}'.format(n3, n4, n5))
