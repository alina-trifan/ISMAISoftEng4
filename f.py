def saveEntries(l):
    with open ('parque.csv', 'a+') as parque_csv:
        writer_csv = csv.writer (parque_csv, delimiter=';')
        for i in range(cont):
            writer_csv.writerow('')