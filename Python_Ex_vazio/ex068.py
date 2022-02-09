from random import randint
from time import sleep
cont = 0
while True:
    resp = int(input('\033[32mDigite um número par ou impar para jogar com a máquina: \033[m'))
    print('\033[33m-=\033[m'*25)
    pi = str(input('\033[36mDigite "P" para par e "I" para ímpar: \033[m')).upper().strip()
    print('\033[33m-=\033[m'*25)
    alea = randint(0,10)
    soma = resp + alea
    if soma % 2 == 0:
        parn = 'par'
    else:
        parn = 'impar'
    if soma % 2 == 0 and pi == 'P':
        print(f'\033[34mA máquina pensou no número {alea} e você pensou no número {resp},\na soma é {soma}, parabéns, {soma} é um número par, você venceu desta vez!\033[m')
    elif soma % 2 != 0 and pi == 'I':
        print(f'\033[34mA máquina pensou no número {alea} e você pensou no número {resp},\na soma é {soma}, parabéns, {soma} você venceu desta vez!\033[m')
    else:
        break
    sleep(2)
    print('\033[33m-=\033[m'*25)
    cont += 1
if cont == 0:
    print(f'\033[35mGAME OVER!!!\033[31m\nA máquina pensou no número {alea} e você pensou no número {resp},\na soma é {soma}, um número {parn},perdeu de primeira !\033[m')
elif cont == 1:
    print(f'\033[35mGAME OVER!!!\033[31m\nA máquina pensou no número {alea} e você pensou no número {resp},\na soma é {soma}, um número {parn},venceu apenas {cont} vez !\033[m')
else:
    print(f'\033[35mGAME OVER!!!\033[31m\nA máquina pensou no número {alea} e você pensou no número {resp},\na soma é {soma}, um número {parn}, venceu {cont} vezes consecutivas !!!!\033[m')
