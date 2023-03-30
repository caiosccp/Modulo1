peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é sua altura? (m) "))
imc = peso / (altura ** 2)
print ("O IMC dessa pessoa é de {:.2F}" .format(imc))

if imc < 18.5:
    print ("CUIDADO!!! Você está abaixo do peso.")
elif imc >= 18.5 and imc < 25:
    print ("PARABÉNS!!! Você está com peso normal.")
elif imc >= 25 and imc < 30:
    print ("CUIDADO!!! Você está acima do peso.")
elif imc > 30:
    print("MUITO CUIDADO!!! Você está obeso(a).")
