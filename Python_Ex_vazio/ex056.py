media_idade = 0
velho = ''
novo = ''
for c in range(1, 5):
    nome = str(input('Digite o nome da {}º pessoa: '.format(c))).strip().capitalize()
    idade = int(input('Digite a idade da {}º pessoa: '.format(c)))
    sexo = str(input('Digite o sexo [M/F] da {}º pessoa: '.format(c))).strip().upper()
    print('=' * 37)
    media_idade += idade / 4
    if c == 1 and sexo =='M':
        velho = idade
        novo = idade
    else:
        if idade > velho:
            velho = nome
        if idade < velho:
            novo = nome
print(velho)

