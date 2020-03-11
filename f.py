def saveEntries(l):
    
    if not operations:
        
        print("Não existem entradas no Parque!")


    else:
        
        i = len(operations)
        with open('parque.csv', newline = '', delimiter = ";") as file:
            doc = csv.writer(file)

            for x in range(i):
                doc.writerow(operations[x])

        print("Foram guardados ",i,"ficheiros.")
        return doc
