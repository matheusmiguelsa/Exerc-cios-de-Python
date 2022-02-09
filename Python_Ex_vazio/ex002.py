i = input('Digite seu nome: ').strip().capitalize()
msg = 'É um prazer te conhecer '
x = i
print('{}{}{}{}{}'.format('\033[0;36m', msg, '\033[4;31m', x, '\033[m'))
