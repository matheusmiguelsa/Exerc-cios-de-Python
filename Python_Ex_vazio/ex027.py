n1 = str(input('Digite seu nome completo: ')).strip()
n2 = n1.title()
n3 = n2.split()
n4 = n3[0]
n5 = n3[-1]
print('Muito prazer em te conhecer!\nSeu primeiro nome é {}\nSeu último nome é {}'.format(n4, n5))
