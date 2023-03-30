def conta_letra(string, letra):
    contador = 0 #começando com 0
    for item in string:
        if item == letra:
            contador += 1
    return contador
print(conta_letra("Vai Corinthians", "a"))