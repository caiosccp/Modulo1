mensagem_criptografada = ['8', '5', '-1', '7', '6', '-1', '8', '4', '-1', '7', '3', '-1', '7', '7', '-1', '6', '5', '-1']
letra = ''
palavra = ''

for i in mensagem_criptografada:

    if i != '-1':
        letra += i
    else:
        palavra += chr(int(letra))
        letra = ''
          
print(palavra)
