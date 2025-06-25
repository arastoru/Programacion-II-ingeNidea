#Codigo de ordenamiento burbuja
def ordenamiento_burbuja(lista):
    n = len(lista)  # Cantidad de elementos en la lista

    for i in range(n - 1):   # Bucle exterior para las pasadas
        hubo_intercambio = False  # Marca si hubo un intercambio en esta pasada

        # Bucle interior para las comparaciones e intercambios
        for j in range(n - 1 - i):  # Cada pasada evita revisar los últimos ya ordenados
            if lista[j] > lista[j + 1]:
                # ¡Intercambio!
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_intercambio = True

        if not hubo_intercambio: # Si no hubo ningún intercambio, la lista ya está ordenada
            break

    return lista  # Opcional: también se puede omitir

if __name__ == "__main__":
    numeros = [6, 3, 8, 2, 5]
    print("Antes:", numeros)
    ordenamiento_burbuja(numeros)
    print("Después Ordenamiento Burbuja:", numeros)

    print("\n--- Ejecutando pruebas con asserts ---")

    # Caso 1: Lista desordenada
    lista1 = [6, 3, 8, 2, 5]
    try:
        ordenamiento_burbuja(lista1)
        assert lista1 == [2, 3, 5, 6, 8], "Fallo en Caso 1: Lista desordenada"
        print("Caso 1 (Lista desordenada): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 2: Lista ya ordenada
    lista2 = [1, 2, 3, 4, 5]
    try:
        ordenamiento_burbuja(lista2)
        assert lista2 == [1, 2, 3, 4, 5], "Fallo en Caso 2: Lista ya ordenada"
        print("Caso 2 (Lista ya ordenada): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 3: Lista ordenada a la inversa (peor caso)
    lista3 = [5, 4, 3, 2, 1]
    try:
        ordenamiento_burbuja(lista3)
        assert lista3 == [1, 2, 3, 4, 5], "Fallo en Caso 3: Lista ordenada a la inversa"
        print("Caso 3 (Lista ordenada a la inversa): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 4: Lista con elementos duplicados
    lista4 = [5, 1, 4, 2, 8, 5, 2]
    try:
        ordenamiento_burbuja(lista4)
        assert lista4 == [1, 2, 2, 4, 5, 5, 8], "Fallo en Caso 4: Lista con elementos duplicados"
        print("Caso 4 (Lista con elementos duplicados): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso borde: Lista vacía
    try:
        assert ordenamiento_burbuja([]) == [], "Fallo en Caso borde: Lista vacía"
        print("Caso borde (Lista vacía): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso borde: Lista con un solo elemento
    try:
        assert ordenamiento_burbuja([42]) == [42], "Fallo en Caso borde: Lista con un solo elemento"
        print("Caso borde (Lista con un solo elemento): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    print("\nPrograma realizado por Franz Almanza")



