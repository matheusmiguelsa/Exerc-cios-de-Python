from random import randint
#wrong way total
cont = 0
tupla = (0,1,2,3,4,5,6,7,8,9)
a = []
for tupla in range(0,5):
    tupla = randint(0, 9)
    a.append(tupla)
b = tuple(a)
print(f'A tupla fica:\n{b}')
print(f'O maior valor é {max(b)}')
print(f'O menor valor é {min(b)}')

# right way

real = (randint(0,9), randint(0,9),randint(0,9),randint(0,9),randint(0,9))
for r in real:
    print(f'{r}', end='')
print(f'\n{max(real)}')
print(min(real))