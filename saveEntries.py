def saveEntries(l):


    matriculas=[]
    parking=open('parque.csv', 'w')
    with parking:
        writer = csv.writer(parking)
        writer.writerows(matriculas)

    duracao=[]
    parking=open('parque.csv', 'w')
    with parking:
        writer = csv.writer(parking)
        writer.writerow(duracao)
