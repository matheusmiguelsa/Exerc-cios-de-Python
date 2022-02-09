from typing import Sized


s1 = int(input('Reta 1: '))
s2 = int(input('Reta 2: '))
s3 = int(input('Reta 3: '))
maior = s1
if s2 > s1 and s2 > s3:
    maior = s2
elif s3 > s1 and s3 > s2:
    maior = s3
menor = s1
if s2 < s1 and s2 < s3:
    menor = s2
elif s3 < s1 and s3 < s2:
    menor = s3
medio = s1
if s3 < s2 < s1 or s1 < s2 < s3:
    medio = s2
elif s2 < s3 < s1 or s1 < s3 < s2:
    medio = s3

if maior - (menor + medio) > 0:
    print('Não é possível formar um triângulo')
else:
    if maior == menor == medio:
            print('Equilátero: todos os lados são iguais')
    elif maior != menor !=medio:
            print('Escaleno: todos os lados são diferentes')
    else:
            print('Isósceles: dois lados iguais, e um é diferente')
            