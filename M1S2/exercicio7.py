valoretiqueta = float(input("Informe o valor conforme a etiqueta: "))
print ("1- Dinheiro | 2- Cartão de crédito | 3- Em duas vezes | 4- Mais de duas vezes")

formadepagamento = float(input("Informe a forma de pagamento: "))

if (formadepagamento == 1):
    dinheiro = valoretiqueta * 0.85
    print ("O valor total pago em dinheiro será de: R$ {:.2F}".format(dinheiro))

elif (formadepagamento == 2):
    cartao = valoretiqueta * 0.90
    print ("O valor total pago via cartão crédito será de: R$ {:.2F}".format(cartao))

elif (formadepagamento == 3):
    print ("O valor total pago em duas vezes será de: R$ {:.2F}".format(valoretiqueta))

elif (formadepagamento == 4):
    parcelado = valoretiqueta * 1.10
    print ("O valor total pago acima de duas vezes será de: R$ {:.2F}".format(parcelado))
