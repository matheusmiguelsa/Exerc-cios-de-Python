continuar = ' '
zero_vinte = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while continuar not in 'N':
   
    while True:
        pedido = int(input('Digite um número entre 1 e 20: '))
        if pedido >=0 and pedido <=20:
            break
        else:
            print('\033[31mvalor inválido\033[m')
    print(zero_vinte[pedido])
    continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if continuar != 'N' and continuar != 'S':
        print('\033[31mDigite uma opção válida\033[m')
    elif continuar == 'N':
        break
