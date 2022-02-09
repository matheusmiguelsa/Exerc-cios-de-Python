a1 = int(input('Digite quantos termos da sequência de Fibonacci você quer mostrar na tela: '))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} -> {t2}', end='')
while cont <= a1:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
