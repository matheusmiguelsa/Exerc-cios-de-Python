bra = ('Corinthians', 'Vasco', 'Flamengo', 'Avai', 'Criciuma', 'Grêmio', 'Cruzeiro', 'Chapecoense', 'Atlético Paranaense','Atlético Goianiense','Atlético Mineiro', 'Santos', 'São Paulo', 'Palmeiras', 'Portuguesa', 'Ponte Preta', 'Fluminense', 'Bahia', 'Fortaleza', 'Ceará')
top_5 = bra[0], bra[2], bra[16], bra[13], bra[12]
bot_4 = bra[1], bra[3:6]
print(f'Os 5 primeiros colocados da tabela são: \n{top_5}')
print(f'Os 4 últimos colocados da tabela são: \n{bot_4}')
print(f'Os 20 colocados da tabela em ordem alfabética são: \n{sorted(bra)}')
for pos, time in enumerate(bra):
    if time =='Chapecoense':
        cabrito = pos + 1
print(f'O time Chapecoense esta na posição {cabrito}º')
