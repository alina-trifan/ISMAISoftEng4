import csv

def saveEntries(l):
    if not operations:
        print("\nNão existem entradas no Parque!")
    else:
        quantidade = len(operations)
        with open('parque.csv','w',newline='',delimiter=";") as file:
            ficheiro = csv.writer(file)
            for i in range(0,quantidade):
                ficheiro.writerow(operations[i])
        print("Foram salvas ",quantidade,"entradas.")
        return ficheiro
