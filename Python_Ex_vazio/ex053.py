frase = str(input('Digite uma frase para saber se ela é um palíndromo: ')).strip().upper()
inverso = ''
separado = frase.split()
junto = ''.join(separado)
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
print('{}'.format(inverso), end='')
print(' {}'.format(junto))
if junto == inverso:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')