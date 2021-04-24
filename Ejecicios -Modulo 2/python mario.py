n = 0
while n < 8:
    numero = int(input('Ingresa numero entero  '))
    validos = [1, 2, 8]
    if numero in validos:
        for i in range(1,numero+1):
            print(" " * (int(numero) - i)  + '#' * int(i))
    else:
        print('entrada invalida')
