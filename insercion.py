import random 

def ordenamiento_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual

    return lista


def run():
    tamaño_lista = int(input("Introduce el tamaño de la lista: "))

    lista = [random.randint(0,100) for i in range(tamaño_lista)]
    print("Lista ordenada:")
    print(lista)
    lista_ordenada = ordenamiento_insercion(lista)
    print("Lista ordenada:")
    print(lista_ordenada)
if __name__ == '__main__':
    run()
    pass
