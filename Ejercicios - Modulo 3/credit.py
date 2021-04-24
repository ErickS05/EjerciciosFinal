intentos = 0
while intentos <7:
    intentos += 1
    tarjeta =input('Ingrese su numero de tarjeta: ')

    inv = tarjeta[::-1]
    cont = 0
    a = 0
    b = 0
    for i in inv:
        n = int(i)
        if cont%2 != 0:
            x = n*2
            if x >9:
                und = x - 10
                a += und + 1
            else:
                a += x

        else:
            b += n

        cont += 1

    suma = a+b

    if suma%10 == 0:
        print('tarjeta valida')
    else: 
        print('tarjeta invalida')

    #Amex
    if tarjeta[0] == '3' and (tarjeta[1] == '4' or tarjeta[1]=='7'):
        print('AMEX\n')
    #mastercard
    elif tarjeta[0] == '5' and (tarjeta[1] == '1' or tarjeta[1] == '2' or tarjeta[1] == '3' or tarjeta[1] == '4' or tarjeta[1] == '5'):
        print('MASTERCARD\n')
    #visa
    elif tarjeta[0] == '4':
        print('VISA\n')
    else:
        print('INVALID\n')