n1 = float(input('informe a 1ª nota: '))
n2 = float(input('informe a 2ª nota: '))

m = (n1 + n2)/ 2

if m == 10:
    print('aprovado com Distinção, média: ', m)
elif m > 7:
    print('aprovado, media: ', m)
else:
    print('reprovado, média: ', m)
