lista = []
mai = 0
men = 0
for valores in range(0, 5):
    lista.append(int(input(f'Digite um valor na posição {valores}: ')))
    if valores == 0:
        mai = men = lista[valores]
    else:
        if lista[valores] > mai:
            mai = lista[valores]
        if lista[valores] < men:
            men = lista[valores]

print('-='*30)
print(lista)
print(f'O maior valor foi {mai} nas posições')

for i, v in enumerate(lista):
    if v == mai:
        print(f'{i}... ', end='')

print(f'\nO menor valor foi {men} nas posições')

for i, v in enumerate(lista):
    if v == men:
        print(f'{i}...', end='')
print()

