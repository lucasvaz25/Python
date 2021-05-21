salAnt = float(input('informe o valor do salário: '))
if salAnt < 281:
    salAtual = salAnt + ((salAnt/100)*20)
    p = 20
elif (salAnt > 280) and (salAnt < 701):
    salAtual = salAnt + ((salAnt/100)*15)
    p = 15
elif (salAnt > 700) and (salAnt < 1501):
    salAtual = salAnt + ((salAnt/100)*10)
    p = 10
elif (salAnt > 1500):
    salAtual = salAnt + ((salAnt/100)*5)
    p = 5
    
print('O salário antes do aumento era: ',salAnt,', sofreu um aumento de ',p,'%, equivalente a ',((salAnt/100)*p),'. Novo salário R$',salAtual,'. ')
