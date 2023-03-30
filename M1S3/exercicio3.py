def soma(*args):
    s= 0
    for num in args:
        s += num
    print(f'Somando os valores {args} temos {s}')

soma(1, 2, 5, 6, 7, 10)