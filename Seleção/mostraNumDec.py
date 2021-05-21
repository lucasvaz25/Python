num = []
for i in range(1,4):
    i = input('informe um numero: ')
    num.append(int(i))


print(sorted(num, key=int, reverse=True))
