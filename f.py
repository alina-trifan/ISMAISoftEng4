def saveEntries(l):
	qtd = len(operations)
	if qtd > 0:
		with open('parque.csv','w',newline='',delimiter=";") as file:
            f_parque = csv.writer(file)
            for i in range(0,qtd):
                f_parque.writerow(operations[i])
        print(qtd,"linhas inseridas")
        return f_parque
	else:
		print("Parque Vazio")