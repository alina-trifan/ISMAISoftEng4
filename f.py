        with open('parque.csv',newline='',delimiter=";") as file:
            f_parque = csv.writer(file)
            for i in range(0,len(operations)):
                f_parque.writerow(operations[i])
        print("Registaram-se",len(operations),"entradas.")
        return ficheiro