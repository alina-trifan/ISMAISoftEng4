class Duracao:

    def validDuration():

        exitFlag = 0
        durationFlag = False

        while True:
            d = input("Digite a duração (0 ou Enter para sair): ")
            if (d!='0' and d!=''): 
                int_d = int(d)     
                if int_d < 0:	
                    print("Valor negativo não é válido.")
                    continue
                elif int_d > 0:
                    d = int_d
                    exitFlag = 0
                    durationFlag = True
                    break
                else:
                    str_d = str(int_d)
                    if (str_d=='0' and str_d==''):
                        exitFlag = 1
                        break
                    else:                     
                        print("Valor inválido")
                        durationFlag = False
                break            
            else:
                exitFlag = 1 
                break
            break	
        return d, durationFlag, exitFlag
