i = str(input('Em que cidade você nasceu? ')).strip()
x1 = i.title()
x2 = x1.split()
x3 = x2[0]
x4 = x3.find('Santo')
if x4 == 0:
    print('Você nasceu em uma cidade que começa com "Santo"')
elif x4 == -1:
    print('Você não nasceu em uma cidade que começa com "Santo"')