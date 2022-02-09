from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nascimento = int(input(f'Digite o ano de nascimento da {c}º pessoa: '))
    idade = atual - nascimento
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Há {} menores de idade\ne {} maiores de idade'.format(totmenor, totmaior))
