import csv

def saveEntries(l):
    cont = len()
    with open('parque.csv',newline='',delimiter=";") as file:
        writer_csv = csv.writer(file)
        for i in range(0, cont):
            writer_csv.writerow()
    return writer_csv
