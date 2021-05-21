salario = float(input("Entre com o salário: "))

if salario < 280:
    porcentagem = 20
    novoSalario = salario + ((porcentagem / 100) * salario)
elif salario > 280 and salario < 700:
    porcentagem = 15
    novoSalario = salario + ((porcentagem / 100) * salario)
elif salario > 700 and salario < 1500:
    porcentagem = 10
    novoSalario = salario + ((porcentagem / 100) * salario)
else:
    porcentagem = 5
    novoSalario = salario + ((porcentagem / 100) * salario)

print("Antigo salário: ", salario)
print("Valor da porcentagem de aumento: ", porcentagem)
print("Valor do aumento: ", novoSalario - salario)
print("Novo salário", novoSalario)
