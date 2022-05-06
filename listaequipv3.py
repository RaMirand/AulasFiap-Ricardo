inventario = [
    ["Impressora", 349.99, 1111, "ENG"], ["Scanner", 147.59, 2222, "ENG"],
    ["Notebook01", 4389.79, 1234, "TI"], ["Notebook02", 4389.79, 1235, "TI"]
]

for elemento in inventario:
    print("Nome........: ", elemento[0])
    print("Valor.......: ", elemento[1])
    print("Serial......: ", elemento[2])
    print("Departamento: ", elemento[3])
    print("")
