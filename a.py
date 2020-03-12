import csv
import operator

carros = []

file = 'ep1.csv'
openFile = open(file)
reader = csv.reader(openFile, delimiter=';')

def importar():
    
    for col in reader:
        
        carros.append(col)
        

    return carros
   

def a():
    carros = importar()
    
    print("Nome do ficheiro: ", file)
    print("Foram importados", len(carros)," registos.")
    



a()

