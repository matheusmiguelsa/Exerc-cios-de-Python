listagem = (
'Pão', 1.50, 'Broa', 2.32, 'lapis', 1.60, 'caneta', 2, 'pincel', 10.50,
'lapiseira', 5, 'borracha', 2.75, 'regua', 20, 'transferidor', 2.50
)
print('-='*20)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-='*20)
for lista in range(0, len(listagem)):
    if lista % 2 == 0:
        print(f'{listagem[lista]:.<30}', end='')
    else:
        print(f'R${listagem[lista]:>7.2f}')
