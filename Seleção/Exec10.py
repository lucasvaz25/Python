turno = input("Que turno você estuda? Digite M-matutino ou V-Vespertino ou N- Noturno: ")

if turno == "m":
    print("Bom Dia!")
elif turno == "v":
    print("Boa Tarde!")
elif turno == "n":
    print("Boa Noite!")
else:
    print("Valor Inválido!")