letraA = float(input("Informe o valor da variável A: "))
letraB = float(input("Informe o valor da variável B: "))
letraC = float(input("Informe o valor da variável C: "))
soma= letraA + letraB

if(soma < letraC):
    print (soma, "Variável A+B foi o resultado de menor valor. ")

if(letraC < soma):
    print (letraC, "Variável C foi o resultado de menor valor. ")
