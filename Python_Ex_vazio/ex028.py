import random
i = int(input('Escreva um número >=0 e <=5: '))
n1 = random.randint(0, 5)
if i == n1:
    print('Parabéns seu sortudo safado, você acertou o número que eu pensei({})'.format(n1))
elif i != 5:
    print('Perdeu pra máquina, tenta de novo marreco!')
