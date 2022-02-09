#contadores
cont_18 = cont_h = cont_m20 = 0
continuar = ''
#while
while True:
    if continuar == 'N':
        break
    print('-=' * 25)
    idade = int(input('Quantos anos: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo [M/F]: ')).upper().strip()[0]
        if sexo != 'M' and sexo != 'F':
            print('\033[33mopção inválida, selecione uma opção válida para continuar\033[m')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('você deseja continuar [S/N]?' )).upper().strip()[0]
        if continuar != 'S' and continuar != 'N':
            print('\033[33mopção inválida, selecione uma opção válida para continuar\033[m')
#homens
    if sexo == 'M':
        cont_h += 1
#18+
    if idade >= 18:
        cont_18 += 1
#mulheres 20-
    if sexo == 'F' and idade < 20:
        cont_m20 += 1
#msg
print(f'Pessoas com mais de 18 anos: {cont_18}')
print(f'Homens cadastrados: {cont_h}')
print(f'Mulheres com menos de 20 anos cadastradas: {cont_m20}')