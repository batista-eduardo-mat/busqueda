import random

def busqueda_binaria(lista, comienzo, final, valor):
    # print(f'buscando {valor} entre {lista[comienzo]} y {lista[final -1]}')
    if comienzo > final:
        return False
        pass
    medio = (comienzo + final ) // 2

    if lista[medio] == valor:
        contador += 1
        return True
        pass
    elif lista[medio] < valor:
        contador += 1
        return busqueda_binaria(lista, medio + 1, final, valor)
        pass
    else:
        contador += 1
        return busqueda_binaria(lista, 0, medio - 1, valor)
        pass
    pass


def run():
    tamaño_lista = int(input("Introduce el tamaño de la lista: "))
    valor = int(input("¿Valor entero que quieres encontrar?: "))

    lista = sorted([random.randint(0,100) for i in range(tamaño_lista)])
    encontrado = busqueda_binaria(lista, 0, len(lista), valor)
    print(lista)
    print(f'El elemento {valor} {"esta" if encontrado else "no esta"}  en la lista ')

if __name__ == '__main__':
    run()
    pass

