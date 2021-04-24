lista1 = 'YTNSHKVEFXRBAUQZCLWDMIPGJO'
lista2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

texto = (input('introduza texto a descrifrar'))

for i in texto:
    contador = 0
    for x in lista2:
        if i == x:
            y = lista1[contador]
            texto = texto.replace(i, y)
        else:
            contador +=1

print(texto)