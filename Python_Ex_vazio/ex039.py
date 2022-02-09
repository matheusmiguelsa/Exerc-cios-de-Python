from datetime import date
i = int(input('Digite seu ano de nascimento: '))
ah = date.today().year
ia = ah - i

if ia < 18:
    print('Você nasceu em {}, tem {} anos em {}, no ano de {} você precisará se alistar'.format(i, ia, ah,  (ia - 18) * -1))
elif ia == 18:
    print('Você tem {} anos em {}, e deve se alistar imediatamente{}!!{}'.format(ia, ah, '\033[31m', '\033[m'))
else:
    print('Você tem {} anos\nVocê já deveria ter se alistado há {} anos\nSeu alistamento deveria ser feito em {}'.format(ia, ia - 18, i + 18))