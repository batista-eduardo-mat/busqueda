import random 

def ordenamiento_mezcla(lista):
    if len(lista) <= 1:
        return lista    
        
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        print(izquierda, '*' * 5, derecha)

        # Recursividad en cada mitad

        ordenamiento_mezcla(izquierda)
        ordenamiento_mezcla(derecha)

        # Iteradores para las dos sublistas

        i = 0
        j = 0

        # Iterador para la lista principal

        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i] 
                i += 1

            else:
                lista[k] = derecha[j]
                j += 1
                pass
            
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1  
            k += 1
            pass

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
            pass

        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)
        return lista  
    

def run():
    tamaño_lista = int(input("Introduce el tamaño de la lista: "))

    lista = [random.randint(0,100) for i in range(tamaño_lista)]
    print("Lista")
    print(lista)
    print("*" * 20)
    print("Lista ordenada:")
    lista_ordenada = ordenamiento_mezcla(lista)
    print(lista_ordenada)

if __name__ == '__main__':
    run()
    pass
