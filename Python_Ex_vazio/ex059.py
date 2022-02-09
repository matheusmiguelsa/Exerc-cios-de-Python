from time import sleep
#menu
print('')
#criar loop finito com while
false = False
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
print('')
while not false:
    escolha = int(input('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\nQual é sua opção? '))
    if escolha == 1:
        print(f'A soma entre {v1} e {v2} é {v1 + v2}')
    elif escolha == 2:
        print(f'O produto entre {v1} e {v2} é {v1 * v2}')
    elif escolha == 3:
        if v1 > v2:
            print(f'O maior entre {v1} e {v2} é {v1}')
        elif v1 < v2:
            print(f'O maior entre {v1} e {v2} é {v2}')
        else:
            print('Os dois valores são iguais')
    elif escolha == 4:
        v1 = int(input('Informe o primeiro valor novamente: '))
        v2 = int(input('Informe o segundo valor novamente: '))
    elif escolha == 5:
        false = True
        print('Finalizande...')
    else:
        print('\033[31mvalor inválido, digite sua opção corretamente!\033[m')
    sleep(2)

#break (msg final)
print('=-=-=-=-=-=-=-=-=')
print('Volte sempre')