#contadores
total = mais_mil = menor = cont = 0
barato = ''
#while
while True:
    produto = str(input('Digite o nome do produto: ')).strip()
    preço = float(input('Digite o valor do produto: R$'))
    cont += 1
    total += preço
    if preço >= 1000:
        mais_mil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
            break
#continuar
    
#total gasto, qts produtos 1000+, + barato
if mais_mil > 1:
    print(f'O total gasto foi R$ {total:.2f}.\n{mais_mil} produtos foram mais caros do que R$ 1000.00.\nO nome do produto mais barato é {barato} que custa R$ {menor:.2f}.')
else:
    print(f'O total gasto foi R$ {total:.2f}.\n{mais_mil} produto foi mais caros do que R$ 1000.00.\nO nome do produto mais barato é {barato} que custa R$ {menor:.2f}.')

