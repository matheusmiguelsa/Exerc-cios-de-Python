resposta = ' '
while resposta != 'F' and resposta != 'M':
    print('\033[31mResposta inválida, digite uma resposta válida para continuar\033[m')
    resposta = input('Você é homem ou mulher [M/F]').upper().strip()[0]
if resposta == 'M':
    print('\033[32mVocê é homem\033[m')
elif resposta == 'F':
    print('\033[32mVocê é mulher\033[m')

