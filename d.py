def printClients(v):
    sort = sorted(vehicles,key=operator.itemgetter(2))
    for row in sort:
        print(f'\t{row[2]} : ({row[0]}, {row[1]})')