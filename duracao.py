import re
import csv

class Duracao:

    def validDuration():

        exitFlag = 0

        while True:
            d = input("Digite a duração (0 ou Enter para sair): ")
            if (d!='0' and d!=''): 
                int_d = int(d)     
                if int_d < 0:	
                    print("Valor negativo não é válido.")
                    continue
                elif int_d > 0:
                    exitFlag = 0
                    break
                else:
                    str_d = str(int_d)
                    if (str_d=='0' and str_d==''):
                        exitFlag = 1
                        break
                    else:                     
                        print("Valor inválido")
                break            
            else:
                exitFlag = 1 
                break	
        return int_d, True, exitFlag
