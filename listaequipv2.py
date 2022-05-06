equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for indice in range(0, len(equipamentos)):
    print("Equipamento..:", (indice+1))
    print("Nome.........:", equipamentos[indice])
    print("Valor........:", valores[indice])
    print("Serial.......:", seriais[indice])
    print("Departamento.:", departamentos[indice])
    print("")

busca = input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print("Equipamento..: ", equipamentos[indice])
        print("Valor........: ", valores[indice])
        print("Serial.......: ", seriais[indice])
        print("Departamento.: ", departamentos[indice])
    else:
        print("Não foi encontrado nenhum equipamento com este nome!")

depreciacao = input("Digite o nome do equipamento a ser depreciado: ")
porc = float(input("Qual a porcetagem de depreciação?: "))
for indice in range(0, len(equipamentos)):
    if depreciacao == equipamentos[indice]:
        print("Valor antigo: ", valores[indice])
        valores[indice] = valores[indice] * (1-porc/100)
        print("Valor novo: ", valores[indice])
    else:
        print("Não foi encontrado nenhum equipamento com este nome!")
