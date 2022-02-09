t = int(input('Digite um número para saber sua tabuada: '))
valor_max = 11
valor_min = 1

for c in range(valor_min, valor_max):
    print(f'{t} X {c:2} = {c * t}')