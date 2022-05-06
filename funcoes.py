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
            print("Novo valor: ", elemento[1])
