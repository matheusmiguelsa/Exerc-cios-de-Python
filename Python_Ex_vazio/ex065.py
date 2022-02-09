'''#while
cont = soma = media = maior = menor = 0
continuar = 'S'
while continuar in 'Ss':
    numero = int(input('Digite um valor: '))
    cont += 1
    soma += numero

#maior e menor
    if cont ==1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
#continuar [S/N]
    continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
#média
media = (f'{(soma / cont):.0f}')
#FIM
print('Foram digitados {} valores, e a média entre eles é {},\no maior valor foi {} e o menor valor foi {}'.format(cont, media, maior, menor))
print('FIM')'''

soma = cont = maior = menor = continuar = 0
continuar = 'S'
while continuar in 'Ss':
    numero = int(input('Digite um número: '))
    cont += 1
    soma += numero
    continuar = str(input('Deseja continuar [S/N]? '))
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
media = (f'{(soma / cont):.2f}')
print(f'Foram digitados {cont} valores, e a média entre eles é {media},\no maior valor foi {maior} e o menor valor foi {menor}')