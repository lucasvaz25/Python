preco = []
print('informe o preço dos produtos:')

for i in range(1,4):
    
    i = input('insira o valor do produto: ')
    preco.append(float(i))


print('o produto de menor valor custa :',min(preco))
