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


def menu():
    return input("<I> - Para inserir um equipamento\n" +
                 "<P> - Para pesquisar um equipamento\n" +
                 "<E> - Para excluir um equipamento\n" +
                 "<L> - Para listar os equipamentos\n" +
                 "O que deseja realizar?: ").upper()


def inserir(dicionario):
    dicionario[input("Digite o ID: ")] = [input("Digite o nome do equipamento: ").upper(),
                                          float(
                                              input("Digite o valor do equipamento: ")),
                                          input(
                                              "Digite o número de serial do equipamento: "),
                                          input("Digite o departamento responsável: ").upper()]
