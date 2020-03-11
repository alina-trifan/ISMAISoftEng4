import csv

def saveEntries(l):
    count = len(operations)
    with open('parque.csv',newline='',delimiter=";") as file:
        writer_csv = csv.writer(file)
        for i in range(0, count):
            writer_csv.writerow(operations[i])
    return writer_csv
