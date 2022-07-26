import random

def busqueda_lineal(lista, valor):
    match  = False
    for elemento in lista:
        if elemento == valor:
            match = True
            break
        pass
    return match
    pass

def run():
    tamaño_lista = int(input("Introduce el tamaño de la lista: "))
    valor = int(input("¿Valor entero que quieres encontrar?: "))

    lista = [random.randint(0,100) for i in range(tamaño_lista)]
    encontrado = busqueda_lineal(lista,valor)
    print(lista)
    print(f'El elemento {valor} {"esta" if encontrado else "no esta"}  en la lista ')

if __name__ == '__main__':
    run()
    pass



