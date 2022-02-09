n1 = str(input('Qual é seu nome completo? ')).strip()
n2 = n1.title()
n3 = 'Silva' in n2
if n3 == True:
    print('Seu nome possui Silva')
elif n3 == False:
    print('Seu nome não possui Silva')