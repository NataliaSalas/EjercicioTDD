def menor(arreglo):
    menor = arreglo[0]
    for elemento in arreglo:
        if elemento < menor:
            menor = elemento
    return menor