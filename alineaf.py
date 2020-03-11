import csv
def saveEntries(l):
        totalOperacoes = len(operations)
        with open('parque.csv','w',newline='',delimiter=";") as file:
            file1 = csv.writer(file)
            for i in range(0,quantidade):
                ficheiro.writerow(operations[i])
        print("Foram salvas ",totalOperacoes,"entradas.")
        return file1
