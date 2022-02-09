from math import radians, sin, cos, tan
i = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(i))
cosseno = cos(radians(i))
tangente = tan(radians(i))
print('o ângulo de {} tem o seno de {:.2f}\no ângulo de {} tem o cosseno de {:.2f}\no ângulo de {} tem a tangente de {:.2f}'.format(i, seno, i, cosseno, i, tangente))
