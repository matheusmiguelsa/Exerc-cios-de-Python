from random import randint
print('1 = pedra\n2 = papel\n3 = tesoura')
i = int(input('Digite um número para jogar com o PC: '))
jj = ('Pedra', 'Papel', 'Tesoura')
jr = randint(0, 2)
if i == 1 and jr == 0:
    print('Você escolheu Pedra, e o PC escolheu Pedra\nEmpate!')
elif i == 1 and jr == 1:
    print('Você escolheu Pedra, e o PC escolheu Papel\nDerrota!')
elif i == 1 and jr == 2:
    print('Você escolheu Pedra, e o PC escolheu Tesoura\nVitória!')
elif i == 2 and jr == 0:
    print('Você escolheu Papel, e o PC escolheu Pedra\nVitória!')
elif i == 2 and jr == 1:
    print('Você escolheu Papel, e o PC escolheu Papel\nEmpate!')
elif i == 2 and jr == 2:
    print('Você escolheu Papel, e o PC escolheu Tesoura\nDerrota!')
elif i == 3 and jr == 0:
    print('Você escolheu Tesoura, e o PC escolheu Pedra\nDerrota!')
elif i == 3 and jr == 1:
    print('Você escolheu Tesoura, e o PC escolheu Papel\nVitória!')
elif i == 3 and jr == 2:
    print('Você escolheu Tesoura, e o PC escolheu Tesoura\nEmpate!')

