#while
fat = 1
n = int(input('Digite um valor para descobrir seu fatorial '))
c=n
print(f'Calculando {n}!: ', end='')
while c > 0:
    print(c, end='')
    print('\033[34m X \033[m' if c > 1  else '\033[34m = \033[m', end='')
    fat *= c
    c -= 1 # esqueci de colocar o -=, por não ter aprendido ainda que funcionava
print(f'''{fat}''')


#for
fat = 1
antes = int(input('Digite um valor para descobrir seu fatorial '))
print(f'Calculando {antes}!: ', end='')
for c in range(antes, 0, -1):
    print(c, end='')
    print('\033[34m X \033[m' if c > 1  else '\033[34m = \033[m', end='')
    fat *= c
print(f'''{fat}''')
