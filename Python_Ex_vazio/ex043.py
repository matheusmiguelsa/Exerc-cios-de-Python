m = float(input('Digite sua massa em quilos: '))
a = float(input('Digite sua altura em metros: '))
imc = m / (a**2)
if imc < 18.5:
    print(' Com {}kg e {:.2f}m, seu IMC é {:.1f}, você está abaixo do peso'.format(m, a, imc))
elif imc >= 18.5 and imc < 25:
    print(' Com {}kg e {:.2f}m, seu IMC é {:.1f}, você está com o peso normal'.format(m, a, imc))
elif imc >= 25 and imc < 30:
    print(' Com {}kg e {:.2f}m, seu IMC é {:.1f}, você está acima do peso'.format(m, a, imc))
elif imc >=30 and imc < 35:
    print(' Com {}kg e {:.2f}m, seu IMC é {:.1f}, você está em obesidade 1'.format(m, a, imc))
elif imc >=35 and imc < 40:
    print(' Com {}kg e {:.2f}m, seu IMC é {:.1f}, você está em obesidade 2'.format(m, a, imc))
elif imc >=40:
    print(' Com {}kg e {:.2f}m, seu IMC é {:.1f}, você está em obesidade 3, ou obesidade mórbida'.format(m, a, imc))
