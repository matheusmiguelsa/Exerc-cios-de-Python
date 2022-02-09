tupla = (int(input('Digite um número: ')), int(input('Digite um número: ')),
int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))

if tupla.count(9) == 0:
    print(f'A tupla não possui o número "9"')
elif tupla.count(9) == 1:
    print(f'A tupla possui {tupla.count(9)} numero "9"')
else:
    print(f'A tupla possui {tupla.count(9)} numeros "9"')

if 3 in tupla:
    print(f'A primeira posição a apresentar o número três é a posição {tupla.index(3)}')
else:
    print('Não foi digitado nenhum valor 3')

print('Os números pares da tupla foram:')

for pares in tupla:
    if pares % 2 == 0:
        print(pares, end=' ')

print('\nfim')