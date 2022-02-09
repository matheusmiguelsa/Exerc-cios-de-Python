tab = 0
while True:
    tab = int(input('Digite um valor para saber sua tabuada: '))
    if tab < 0:
        break
    
    for fator in range(1,11):
        print(f'{tab} X  {fator} = {tab * fator}')
    print('-='*25)
