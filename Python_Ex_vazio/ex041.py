from datetime import date
atual = date.today().year
i = int(input('Digite seu ano de nascimento para descobrir sua categoria:'))
c = str({})
id = atual - i
if id <= 9:
    c = 'Mirim'
elif id <=14:
    c = 'Infantil'
elif id <= 19:
    c = 'Junior'
elif id <= 25:
    c = 'Sênior'
else:
    c = 'Master'
print('A categoria de um atleta de {} anos é {}'.format(id, c))
