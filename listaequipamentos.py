inventario = []
resposta = "S"

while resposta == "S":
    inventario.append(input("Equipamento: ").upper())
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número de série: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for elemento in inventario:
    print(elemento)
