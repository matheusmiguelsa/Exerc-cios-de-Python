i = float(input('Digite uma distância em metros: '))
km = i/1000
hm = i/100
dam = i/10
dm = i/1
cm = i/0.1
mm = i/0.01
print('{}A medida de {} corresponde a: \n {}km \n {}hm \n {}dam \n {:.0f}dm \n {:.0f}cm \n {:.0f}mm{}'.format('\033[7m', i, '\033[7m', km, '\033[7m', hm, '\033[7m', dam, '\033[7m', '\033[7m', dm, '\033[7m', cm, '\033[7m', mm, '\033[m'))
