from time import sleep
subtrai = 0
while True:
    valor = int(input('Digite o valor a ser sacado: R$'))
    ced200 = valor // 200
    ced100 = (valor % 200) // 100
    ced50 = (valor % 100) // 50
    ced20 = (valor % 50) // 20
    ced10 = ((valor % 50) % 20) // 10
    ced5 = ((valor % 20) % 10) // 5
    ced2 = ((valor % 10) %5) // 2
    ced1 = ((valor % 5) % 2) // 1

    print(f'Para sacar R${valor:.2f}, serão necessárias:')

    if ced200 != 0:
        print(f'{ced200} cédulas de \033[m200\033[m')
    if ced100 != 0:
        print(f'{ced100} cédulas de \033[36m100\033[m')
    if ced50 != 0:
        print(f'{ced50} cédulas de \033[31m50\033[m')
    if ced20 != 0:
        print(f'{ced20} cédulas de \033[33m20\033[m')
    if ced10 != 0:
        print(f'{ced10} cédulas de \033[31m10\033[m')
    if ced5 != 0:
        print(f'{ced5} cédulas de \033[35m5\033[m')
    if ced2 != 0:
        print(f'{ced2} cédulas de \033[34m2\033[m')
    if ced1 != 0:
        print(f'{ced1} cédulas de \033[32m1\033[m')
        
    break
print('Volte sempre ao banco do milhão, tenha um bom dia!!')


