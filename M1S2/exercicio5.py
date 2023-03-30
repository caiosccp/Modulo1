altura = float(input("Informe sua altura = "))

print ("1-Homem ou 2-Mulher")

sexo = int(input("Informe seu sexo = "))

if(sexo == 1):
    pesoideal = 72.7 * altura - 58
    print ("Seu peso ideal é de ", pesoideal,"KG.")

elif(sexo == 2):
    pesoideal = 62.1 * altura - 44.7
    print ("Seu peso ideal é de ", pesoideal,"KG.")

else:
    print ("Erro! Insira um valor válido em 'sexo'.")
