from random import choice
i = str(input('Digite o primeiro aluno: '))
o = str(input('Digite o segundo aluno: '))
p = str(input('Digite o terceiro aluno: '))
q = str(input('Digite o quarto aluno: '))
x = [i, o, p, q]
xy = choice(x)
print('O aluno escolhido foi {}'.format(xy))