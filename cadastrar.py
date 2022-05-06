from pandas import period_range
from funcoes import menu
from funcoes import inserir

equipamentos = {}
opcao = menu()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(equipamentos)
    opcao = menu()
