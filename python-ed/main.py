from vetores import vetor

print(30 * '-', 'MENU', 30* '-')
print('1. Vetores')
print('2. Listas Ligadas')

menu = int(input('Informe a opção desejada:'))

if menu == 1:
    vetor_teste = vetor.Vetor(0)
#    vetor_teste.inserir_elemento_posicao(1,0)
#    vetor_teste.inserir_elemento_posicao(3,1)
#    vetor_teste.inserir_elemento_final(1)
#    vetor_teste.inserir_elemento_final(2)
#    vetor_teste.inserir_elemento_final(3)
#    vetor_teste.inserir_elemento_final(4)
    vetor_teste.inserir_elemento_posicao(1, 0)
    vetor_teste.inserir_elemento_posicao(2, 1)
    vetor_teste.inserir_elemento_posicao(3, 2)
    vetor_teste.inserir_elemento_posicao(4, 2)
    print(vetor_teste.listar_elemento(0))
    print(vetor_teste.listar_elemento(1))
    print(vetor_teste.listar_elemento(2))
    print(vetor_teste.listar_elemento(3))
    print(vetor_teste.contem(5))

    print(vetor_teste.tamanho_vetor())
    print(vetor_teste)

    print(vetor_teste.indice(4))