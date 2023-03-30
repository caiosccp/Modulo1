def imprime_ate_zero(numero):
    print(numero)
    if numero > 0:
        imprime_ate_zero(numero-1)

imprime_ate_zero(3)
# 3
# 2
# 1
# 0
# print (3)
# print (2)
# print (1)
# print (0)