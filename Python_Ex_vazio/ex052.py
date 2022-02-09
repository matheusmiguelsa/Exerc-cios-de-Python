numero_primo = int(input('Digite um número para saber se ele é primo: '))
cont = 0
for c in range(1, numero_primo + 1):
    if numero_primo % c == 0:
        cont += 1
        print('{}{}{}'.format('\033[31m', c, '\033m'), end=' ')
    else:
        print('{}{}{}'.format('\033[34m', c, '\033[m'), end=' ')
if cont > 2:
    print(f'\n\033[m{numero_primo} não é um número primo, pois é divisível por {cont} números')
elif cont == 1:
    print(f'\n\033[m{numero_primo} é um número primo, pois é divisível por {cont} número')
else:
    print(f'\n\033[m{numero_primo} é um número primo, pois é divisível por {cont} números')