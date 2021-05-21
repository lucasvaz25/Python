ph = float(input('Informe o valor da hora trabalhada: '))
ht = float(input('Informe as horas trabalhadas: '))
sal = (ph * ht)
ir = (sal/100) * 11
inss = (sal/100) * 8
sind = (sal/100) * 5
salliq = sal - (ir + inss + sind)
print('Salario bruto: ', sal)
print('------------------------------------------')
print('Valor pago ao INSS: ', inss)
print('------------------------------------------')
print('Valor pago ao Sindicato: ', sind)
print('------------------------------------------')
print('Salario líquido: ', salliq)
