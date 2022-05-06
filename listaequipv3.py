from funcoes import *

inventario = [
    ["Impressora", 349.99, 1111, "ENG"], ["Scanner", 147.59, 2222, "ENG"],
    ["Notebook01", 4389.79, 1234, "TI"], ["Notebook02", 4389.79, 1235, "TI"]
]
valores = []

for elemento in inventario:
    print("Nome........: ", elemento[0])
    print("Valor.......: ", elemento[1])
    print("Serial......: ", elemento[2])
    print("Departamento: ", elemento[3])
    print("")

for elemento in inventario:
    valores.append(elemento[1])
if len(valores) > 0:
    print("O equipamento mais caro em estoque custou R${}".format(max(valores)))
    print("O equipamento mais barato em estoque custou R${}".format(min(valores)))
    print("O valor total em equipamentos em estoque é de R${}".format(sum(valores)))

busca(inventario)

depre = 10
depreciar(inventario, depre)
