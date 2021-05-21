
lt = 18
v = 80.0
m = float(input('informe o tamanho da area a ser pintada: '))
qlt = (m / 3)
if qlt < 18:
   tlt = 1
else:
   tlt = qlt / lt
   if not tlt == int(tlt):
       tlt = int(tlt + 1)
vt = tlt * v
print('a quantidade de latas de tintas necessárias é:', tlt,', e o valor total é:',vt)
