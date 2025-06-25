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



#Codigo ordenamiento por insercion
def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        valor_actual = lista[i]  # La "carta" que vamos a insertar
        posicion_actual = i

        # Desplazar elementos mayores hacia la derecha
        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        # Insertar la "carta" en su hueco correcto
        lista[posicion_actual] = valor_actual

    return lista

if __name__ == "__main__":
    numeros = [6, 3, 8, 2, 5]
    print("Antes:", numeros)
    ordenamiento_insercion(numeros)
    print("Después Ordenamiento Inserción:", numeros)

    print("\n--- Ejecutando pruebas con asserts ---")

    # Caso 1: Lista desordenada
    lista1 = [6, 3, 8, 2, 5]
    try:
        # No imprimimos "Antes" y "Después" para cada caso de prueba aquí,
        # ya que la salida principal ya lo hace.
        ordenamiento_insercion(lista1)
        assert lista1 == [2, 3, 5, 6, 8], "Fallo en Caso 1: Lista desordenada"
        print("Caso 1 (Lista desordenada): SUCCESS")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 2: Lista ya ordenada
    lista2 = [1, 2, 3, 4, 5]
    try:
        ordenamiento_insercion(lista2)
        assert lista2 == [1, 2, 3, 4, 5], "Fallo en Caso 2: Lista ya ordenada"
        print("Caso 2 (Lista ya ordenada): SUCCESS")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 3: Lista ordenada a la inversa (peor caso)
    lista3 = [5, 4, 3, 2, 1]
    try:
        ordenamiento_insercion(lista3)
        assert lista3 == [1, 2, 3, 4, 5], "Fallo en Caso 3: Lista ordenada a la inversa"
        print("Caso 3 (Lista ordenada a la inversa): SUCCESS")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 4: Lista con duplicados
    lista4 = [5, 1, 4, 2, 8, 5, 2]
    try:
        ordenamiento_insercion(lista4)
        assert lista4 == [1, 2, 2, 4, 5, 5, 8], "Fallo en Caso 4: Lista con duplicados"
        print("Caso 4 (Lista con duplicados): SUCCESS")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso borde: Lista vacía
    try:
        assert ordenamiento_insercion([]) == [], "Fallo en Caso borde: Lista vacía"
        print("Caso borde (Lista vacía): SUCCESS")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso borde: Lista con un solo elemento
    try:
        assert ordenamiento_insercion([42]) == [42], "Fallo en Caso borde: Lista con un solo elemento"
        print("Caso borde (Lista con un solo elemento): SUCCESS")
    except AssertionError as e:
        print(f"Error: {e}")

print("\nPrograma realizado por Franz Almanza")


#Codigo Merge Sort
def merge_sort(lista):
  # Paso Vencer (Condición Base de la Recursividad):
  if len(lista) <= 1:
      return lista

  # Paso 1: DIVIDIR
  medio = len(lista) // 2
  mitad_izquierda = lista[:medio]
  mitad_derecha = lista[medio:]

  # Paso 2: VENCER (Recursión)
  izquierda_ordenada = merge_sort(mitad_izquierda)
  derecha_ordenada = merge_sort(mitad_derecha)

  # Paso 3: COMBINAR
  print(f"Mezclaría {izquierda_ordenada} y {derecha_ordenada}")
  return merge(izquierda_ordenada, derecha_ordenada)

def merge(izquierda, derecha):
  resultado = []
  i = j = 0

  # Comparar elementos de izquierda y derecha uno por uno
  while i < len(izquierda) and j < len(derecha):
      if izquierda[i] < derecha[j]:
          resultado.append(izquierda[i])
          i += 1
      else:
          resultado.append(derecha[j])
          j += 1

  # Agregar cualquier elemento restante
  resultado.extend(izquierda[i:])
  resultado.extend(derecha[j:])

  return resultado

# --- Prueba ---
lista_prueba = [8, 3, 5, 1]
print("Lista original:", lista_prueba)
resultado = merge_sort(lista_prueba)
print("Lista ordenada:", resultado)

# --- Pruebas automatizadas ---
assert merge_sort([]) == []                         # Lista vacía
assert merge_sort([1]) == [1]                       # Lista con un solo elemento
assert merge_sort([5, 2]) == [2, 5]                  # Lista con dos elementos
assert merge_sort([3, 1, 2]) == [1, 2, 3]            # Lista con tres elementos desordenados
assert merge_sort([10, 5, 3, 8, 6, 2]) == [2, 3, 5, 6, 8, 10]  # Lista par
assert merge_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]  # Lista en orden descendente
assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]  # Lista ya ordenada
assert merge_sort([4, 2, 2, 4, 1]) == [1, 2, 2, 4, 4]  # Lista con elementos repetidos
assert merge_sort([100, -50, 0, 50, -100]) == [-100, -50, 0, 50, 100]  # Lista con enteros negativos y positivos
assert merge_sort([2.5, 1.2, 3.8]) == [1.2, 2.5, 3.8]  # Lista con flotantes
print("¡Todas las pruebas con assert pasaron correctamente!")
print("\nPrograma realizado por Franz Almanza")


#Codigo Matrices
# 1. Crear la matriz de 3x3
teclado = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 2. Imprimir la matriz completa
print("Matriz original:")
for fila in teclado:
    print(fila)

# 3. Acceder a elementos específicos
print("\nNúmero en el centro:", teclado[1][1])  # 5
print("Número en la esquina inferior derecha:", teclado[2][2])  # 9

# 4. Modificar el número en la esquina superior izquierda (1 por un 0)
teclado[0][0] = 0

# 5. Imprimir la matriz modificada
print("\nMatriz modificada:")
for fila in teclado:
    print(fila)

# Usamos el teclado modificado del ejercicio anterior
teclado = [
    [0, 8, 9],
    [4, 5, 6],
    [1, 2, 3]
]

print("Matriz como cuadrícula:")
for fila in teclado:
    for elemento in fila:
        print(elemento, end="\t")  # Imprimir sin salto de línea, separado por tabulador
    print()  # Salto de línea al terminar cada fila



# Crear matriz 5x5 con bucles anidados
matriz_ceros = []
for i in range(5):
    fila = []
    for j in range(5):
        fila.append(0)
    matriz_ceros.append(fila)

print("\nMatriz 5x5 llena de ceros (con bucles):")
for fila in matriz_ceros:
    print(fila)
print("\nFranz Almanza - FIN DEL PROGRAMA DE EJERCICOS DE MATRICES")


# Codigo sumar todo elementos de una matriz
def sumar_total_matriz(matriz):

    # matriz = [[1, 2], [3, 4]]
    # resultado = 10

    total = 0
    for fila in matriz:
        for elemento in fila:
            total += elemento
    return total

# Función para probar que sumar_total_matriz funciona correctamente
def probar_suma_total():
    print("--- Probando sumar_total_matriz ---")

    # Caso 1: matriz normal
    m1 = [[1, 2, 3], [4, 5, 6]]
    try:
        assert sumar_total_matriz(m1) == 21, "Fallo en Caso 1: Matriz normal"
        print("Caso 1 (Matriz normal): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 2: matriz con negativos y ceros
    m2 = [[-1, 0, 1], [10, -5, 5]]
    try:
        assert sumar_total_matriz(m2) == 10, "Fallo en Caso 2: Matriz con negativos y ceros"
        print("Caso 2 (Matriz con negativos y ceros): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 3: Matriz con una fila vacía
    m3 = [[]]
    try:
        assert sumar_total_matriz(m3) == 0, "Fallo en Caso 3: Matriz con una fila vacía"
        print("Caso 3 (Matriz con una fila vacía): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 4: Matriz completamente vacía
    m4 = []
    try:
        assert sumar_total_matriz(m4) == 0, "Fallo en Caso 4: Matriz completamente vacía"
        print("Caso 4 (Matriz completamente vacía): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 5: Matriz de un solo elemento
    m5 = [[42]]
    try:
        assert sumar_total_matriz(m5) == 42, "Fallo en Caso 5: Matriz de un solo elemento"
        print("Caso 5 (Matriz de un solo elemento): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    print("Todas las pruebas para sumar_total_matriz han finalizado")

# Llamamos a la función de pruebas
if __name__ == "__main__":
    probar_suma_total()



#Codigo para sumar por fila en matriz
# Definimos la función que suma los elementos por cada fila de la matriz
def sumar_por_filas(matriz):
    """
    Esta función recibe una matriz (lista de listas)
    y devuelve una lista con la suma de cada fila.

    Ejemplo:
    matriz = [[1, 2, 3], [4, 5, 6]]
    resultado = [6, 15]
    """
    resultado = []
    for fila in matriz:
        suma_fila = sum(fila)  # Suma todos los elementos de la fila
        resultado.append(suma_fila)
    return resultado

# Función de prueba para verificar que sumar_por_filas funciona correctamente
def probar_suma_por_filas():
    print("\n Probando sumar_por_filas")

    # Caso 1: matriz con 3 filas y 3 columnas
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    try:
        assert sumar_por_filas(m1) == [6, 15, 24], "Fallo en Caso 1: Matriz con 3x3"
        print("Caso 1 (Matriz 3x3): success")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 2: matriz con pares repetidos
    m2 = [[10, 10], [20, 20], [30, 30]]
    try:
        assert sumar_por_filas(m2) == [20, 40, 60], "Fallo en Caso 2: Matriz con pares repetidos"
        print("Caso 2 (Matriz con pares repetidos): success")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 3: matriz con números negativos
    m3 = [[-1, -2], [0, 5], [-3, 3]]
    try:
        assert sumar_por_filas(m3) == [-3, 5, 0], "Fallo en Caso 3: Matriz con números negativos"
        print("Caso 3 (Matriz con números negativos): success")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 4: matriz con filas de diferente longitud (aunque no es una matriz "regular", la función lo maneja)
    m4 = [[1, 2], [3, 4, 5], [6]]
    try:
        assert sumar_por_filas(m4) == [3, 12, 6], "Fallo en Caso 4: Matriz con filas de diferente longitud"
        print("Caso 4 (Matriz con filas de diferente longitud): success")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 5: matriz vacía
    m5 = []
    try:
        assert sumar_por_filas(m5) == [], "Fallo en Caso 5: Matriz vacía"
        print("Caso 5 (Matriz vacía): success")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 6: matriz con filas vacías
    m6 = [[], [], []]
    try:
        assert sumar_por_filas(m6) == [0, 0, 0], "Fallo en Caso 6: Matriz con filas vacías"
        print("Caso 6 (Matriz con filas vacías): success")
    except AssertionError as e:
        print(f"Error: {e}")

    print("Todas las pruebas para sumar_por_filas han finalizado")

# Llamamos a la función para ejecutar las pruebas
if __name__ == "__main__":
    probar_suma_por_filas()

print("\nPrograma realizado por Franz Almanza")




#Codigo para sumar diagonal en matriz
# Definimos la función que suma los elementos de la diagonal principal de una matriz cuadrada
def sumar_diagonal_principal(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]  # Accede al elemento en la posición (i, i)
    return suma

# Función de prueba para verificar que sumar_diagonal_principal funciona correctamente
def probar_suma_diagonal_principal():
    print("\nPrueba de sumar diagonal")

    # Caso 1: matriz 3x3 con números consecutivos
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    try:
        assert sumar_diagonal_principal(m1) == 15, "Fallo en Caso 1: Matriz 3x3 con números consecutivos"
        print("Caso 1 (Matriz 3x3): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 2: matriz 2x2 con ceros y valores definidos
    m2 = [[10, 0], [0, 20]]
    try:
        assert sumar_diagonal_principal(m2) == 30, "Fallo en Caso 2: Matriz 2x2 con ceros y valores definidos"
        print("Caso 2 (Matriz 2x2): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 3: matriz 1x1
    m3 = [[5]]
    try:
        assert sumar_diagonal_principal(m3) == 5, "Fallo en Caso 3: Matriz 1x1"
        print("Caso 3 (Matriz 1x1): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 4: Matriz con números negativos
    m4 = [[-1, 2], [3, -4]]
    try:
        assert sumar_diagonal_principal(m4) == -5, "Fallo en Caso 4: Matriz con números negativos" # -1 + (-4) = -5
        print("Caso 4 (Matriz con números negativos): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 5: Matriz de 4x4
    m5 = [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]]
    try:
        assert sumar_diagonal_principal(m5) == 10, "Fallo en Caso 5: Matriz 4x4" # 1+2+3+4 = 10
        print("Caso 5 (Matriz 4x4): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    print("Todas las pruebas para sumar_diagonal_principal han finalizado")

# Llamamos a la función para ejecutar las pruebas
if __name__ == "__main__":
    probar_suma_diagonal_principal()
print("\nPrograma realizado por Franz Almanza")




