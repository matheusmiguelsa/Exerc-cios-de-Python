soma = 0
cont = 0

for c in range(1, 7):
    valores = int(input('Digite o {}º valor: '.format(c)))
    if valores % 2 == 0:
        soma += valores
        cont += 1

if cont > 1:
    print(f'A soma dos {cont} números pares é {soma}')
elif cont == 1:
    print(f'A soma de {cont} número par é {soma}')
else:
    print(f'Não há número par indicado')