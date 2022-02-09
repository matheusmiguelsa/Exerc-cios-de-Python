#while
soma = pare = cont = 0
pare = int(input('Digite um número para ser somado (999 para parar): '))
while True:
    if pare == 999:
        break
    soma += pare
    cont += 1
    pare = int(input('Digite um número para ser somado (999 para parar): '))
    
#msg de fim
print(f'A soma dos {cont} números apresentados é {soma}')
print('FIM')