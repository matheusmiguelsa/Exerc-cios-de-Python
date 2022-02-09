cont = soma = 0
num = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
if cont > 1:
    print(f'Foram digitados {cont} números e a soma deles foi {soma}')
else:
    print(f'Foi digitado {cont} número e a soma dele foi {soma}')