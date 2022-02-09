n1 = float(input('Qual a distância da sua viagem em Km? '))
n2 = n1*0.50
n3 = n1*0.45
print('Você está prestes a fazer uma viagem de {}Km!'.format(n1))
#if n1 > 200:
 #   print('O valor a pagar é de R${}'.format(n3))
#else:
  #  print('O valor a pagar é de R${:.2f}'.format(n2))
preço = n3 if n1 > 200 else n2
print('O preço da sua viagem de {}Km é de R${:.2f}'.format(n1, preço))