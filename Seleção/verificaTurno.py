print('* Digite M - matutino, V - vespertino ou N - noturno *')
t = str(input('informe o turno em que estuda: ')).upper()
if t == 'M':
    print('Bom Dia!')
elif t == 'V':
    print('Boa Tarde!')
elif t == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!!')
