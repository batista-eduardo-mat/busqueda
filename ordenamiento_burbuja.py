from os import listxattr
import random

def ordenamiento_burbuja(lista):
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j + 1 ] = lista[j + 1], lista[j]
                pass
            pass
        pass
    pass
    return lista


def run():
    tamaño_lista = int(input("Introduce el tamaño de la lista: "))

    lista = [random.randint(0,100) for i in range(tamaño_lista)]
    print("Lista ordenada:")
    print(lista)
    lista_ordenada = ordenamiento_burbuja(lista)
    print("Lista ordenada:")
    print(lista_ordenada)
if __name__ == '__main__':
    run()
    pass

