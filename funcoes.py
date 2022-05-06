def busca(lista):
    busca = input("Digite o nome do equipamento que deseja buscar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Equipamento..: ", elemento[0])
            print("Valor........: ", elemento[1])
            print("Serial.......: ", elemento[2])
            print("Departamento.: ", elemento[3])


def depreciar(lista):
    depreciacao = input("Digite o nome do equipamento que será depreciado: ")
    porc = float(input("Digite o percentual de depreciação: "))
    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] = elemento[1] * (1-porc/100)
            elemento[1] = "{:.2f}".format(elemento[1])
            print("Novo valor: ", elemento[1])


def excluir(lista):
    serial = int(
        input("Informe o serial do equipamento que deseja excluir da lista: "))
    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)
    print(lista)

# def informacoes(lista):
#     #
