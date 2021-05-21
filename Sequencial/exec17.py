import math
lt = 18
gl = 3.6
v = 80.0
vg = 25.0
mi = float(4 * gl)

    
m = float(input('informe o tamanho da area a ser pintada: '))
folga = ((m/6)/100) *10
qlt = (m / 6) + folga

if qlt <= 18:
   tlt = 1
else:
   tlt = int(math.ceil(qlt / lt))
   x = math.floor(qlt / lt)
   dif = x - (qlt / lt)
   if dif <= mi:
      if dif <= gl:
         a = 1
      else:
         a = int(math.ceil(dif / gl))
      
if qlt <= gl:
   tgl = 1
else:
   tgl = (math.ceil(qlt / gl))



tl = x * v
tg = a * vg
vt = tlt * v
vtg = tgl * vg
print('a quantidade de latas de tintas necessárias é:', tlt,', e o valor total é:',vt)
print('a quantidade de galões de tintas necessárias é:', tgl,', e o valor total é:',vtg)
print('a quantidade de latas:',x,',quantidade de galoes:', a,', e o valor total é:',(tl + tg))
