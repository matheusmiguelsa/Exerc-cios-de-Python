from random import randint
lista = randint(0, 10)
acertou = False
print(lista)
cont = 0
while not acertou:
    a = int(input('Digite um número para adivinhar qual número o computador pensou: '))
    cont += 1
    if lista == a:
        acertou = True
    else:
        if a > lista:
            print('Seu palpite foi maior que o número escolhido')
        else:
            print('Seu palpite foi menor que o número escolhido')
print(f'Acertou, mas demorou {cont} tentativas')
