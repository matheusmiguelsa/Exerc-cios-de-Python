tupla = (
    'casa', 'quarto', 'apartamento', 'pescar', 'gosto', 'lol', 'corki',
    'python', 'biologia', 'programacao',
    'linux', 'casamento', 'noivado'
)
for tuplinhas in tupla:
    print(f'\nNa palavra {tuplinhas} temos:', end=' ')
    for letras in tuplinhas:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
    '''if 'a' in tuplinhas:
        print('a', end=' ')
    if 'e' in tuplinhas:
        print('e', end=' ')
    if 'i' in tuplinhas:
        print('i', end=' ')
    if 'o' in tuplinhas:
        print('o', end=' ')
    if 'u' in tuplinhas:
        print('u', end=' ')
print('\nFIM')'''