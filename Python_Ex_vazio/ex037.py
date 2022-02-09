n = int(input('Digite um valor inteiro em base decimal para saber seu valor em outras bases: '))
b1 = input('Digite a base de conversão (binária, octal ou hexadecimal): ').strip()
b2 = b1.capitalize()
if b2 == 'Binária' or b2 == 'Binaria' or b2 == 'Binário' or b2 == 'Binario':
    print('O valor informado convertido para base binária é {}'.format(bin(n) [2:]))
elif b2 == 'Octal':
    print('O valor informado convertido para base octal é {}'.format(oct(n) [2:]))
elif b2 == 'Hexadecimal':
    print('O valor informado convertido para base hexadecimal é {}'.format(hex(n) [2:]))
else:
    print('Opção inválida')
