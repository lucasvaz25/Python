nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))

media = (nota1 + nota2) / 2

if media > 9 and media <= 10:
    print("APROVADO! - Conceito A!")
elif media > 7.5 and media <= 9:
    print("APROVADO! - Conceito B!")
elif media > 6 and media <= 7.5:
    print("APROVADO! - Conceito C!")
elif media > 4 and media <= 6:
    print("REPROVADO! Conceito D!")
elif media > 0 and media <= 4:
    print("REPROVADO! Conceito E!")
else:
    print("Valor Inválido!")

print("As notas foram: ", nota1, "primeiro bimestre e", nota2, "do segundo bimestre.")
print("A média é: ", media)