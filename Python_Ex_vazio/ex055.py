maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Digite a massa da {p}º pessoa em quilos: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))