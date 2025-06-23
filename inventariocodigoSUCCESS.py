import os

def clear_screen():
    """Borra la pantalla de la consola."""
    # Para sistemas Unix/Linux/macOS
    if os.name == 'posix':
        _ = os.system('clear')
    # Para Windows
    else:
        _ = os.system('cls')

def esperar_tecla():
    """Espera a que el usuario presione una tecla."""
    input("\nPresione Enter para continuar...")

def inventario_de_productos():
    productos = []  # Lista para nombres de productos
    cantidades = []  # Lista para cantidades de productos
    
    while True:
        # Menú de opciones
        print('      ***************************************')
        print('      * Menú de Inventario        *')
        print('      ***************************************')
        print('      1. Agregar nuevo producto')
        print('      2. Mostrar todos los productos')
        print('      3. Buscar un producto')
        print('      4. Actualizar cantidad de un producto')
        print('      5. Salir')
        print('      ***************************************')
        
        try:
            opcion = int(input('Ingrese una opción (del 1 al 5): '))
        except ValueError:
            clear_screen()
            print('*****************************************************************')
            print('     Entrada inválida. Por favor, ingrese un número del 1 al 5.')
            print('*****************************************************************')
            esperar_tecla()
            clear_screen()
            continue # Vuelve al inicio del bucle

        if opcion == 1:
            # Agregar nuevo producto
            nombre_producto = input('Ingrese el nombre del producto: ')
            try:
                cantidad = int(input('Ingrese la cantidad del producto: '))
                if cantidad < 0:
                    raise ValueError("La cantidad no puede ser negativa.")
            except ValueError:
                clear_screen()
                print('*****************************************************************')
                print('     Cantidad inválida. Por favor, ingrese un número entero positivo.')
                print('*****************************************************************')
                esperar_tecla()
                clear_screen()
                continue

            productos.append(nombre_producto)
            cantidades.append(cantidad)
            
            clear_screen()
            print('      ***************************************')
            print('      * Producto agregado correctamente !   *')
            print('      ***************************************')
            print('')
            esperar_tecla()
            clear_screen()

        elif opcion == 2:
            # Mostrar todos los productos
            clear_screen()
            print(' *******************************************')
            print('             LISTADO DE PRODUCTOS            ')
            print(' *******************************************')
            print(' Item        Producto            Cantidad ')
            print(' -------------------------------------------')
            
            if not productos:
                print('       No hay productos en el inventario.')
            else:
                for i in range(len(productos)):
                    # Usamos f-strings para un formato más limpio
                    print(f"({i+1})         {productos[i]:<15} {cantidades[i]:>10}")
            
            print(' -------------------------------------------')
            esperar_tecla()
            clear_screen()

        elif opcion == 3:
            # Buscar un producto
            buscar_producto = input('Ingrese el nombre del producto a buscar: ')
            encontrado = False
            
            clear_screen()
            print(' *******************************************')
            print('             RESULTADO DE LA BUSQUEDA        ')
            print(' *******************************************')
            print(' Item        Producto            Cantidad ')
            print(' -------------------------------------------')
            
            for i in range(len(productos)):
                if productos[i].lower() == buscar_producto.lower(): # Búsqueda insensible a mayúsculas/minúsculas
                    print(f"({i+1})         {productos[i]:<15} {cantidades[i]:>10}")
                    encontrado = True
            
            print(' -------------------------------------------')
            if not encontrado:
                print('      ***************************************')
                print('      * Producto no encontrado !!!!     *')
                print('      ***************************************')
            
            esperar_tecla()
            clear_screen()

        elif opcion == 4:
            # Actualizar cantidad de un producto
            buscar_producto = input('Ingrese el nombre del producto a actualizar: ')
            encontrado = False
            
            clear_screen()
            for i in range(len(productos)):
                if productos[i].lower() == buscar_producto.lower(): # Búsqueda insensible a mayúsculas/minúsculas
                    encontrado = True
                    print(f"Se ha encontrado el producto: {productos[i]}")
                    try:
                        nueva_cantidad = int(input(f'Ingrese la nueva cantidad para el producto con nro de item: ({i+1}): '))
                        if nueva_cantidad < 0:
                            raise ValueError("La cantidad no puede ser negativa.")
                        cantidades[i] = nueva_cantidad
                        print('      ***************************************')
                        print('        Cantidad actualizada correctamente.')
                        print('      ***************************************')
                        print('')
                    except ValueError:
                        print('*****************************************************************')
                        print('     Cantidad inválida. Por favor, ingrese un número entero positivo.')
                        print('*****************************************************************')
                    break # Salir del bucle una vez que el producto es encontrado y actualizado
            
            if not encontrado:
                print('      ***************************************')
                print('            Producto no encontrado.        ')
                print('      ***************************************')
            
            esperar_tecla()
            clear_screen()

        elif opcion == 5:
            # Salir
            clear_screen()
            print('*****************************************************************')
            print('* GRACIAS POR UTILIZAR UPDS-INVENTARIOS V1.0.         *')
            print('* *')
            print('* PROGRAMACION BÁSICA UPDS                      *')
            print('* COPYRIGHT  @2025                              *')
            print('* *')
            print('*****************************************************************')
            break # Sale del bucle principal

        else:
            clear_screen()
            print('*****************************************************************')
            print('     Opción inválida, por favor intente de nuevo.')
            print('*****************************************************************')
            esperar_tecla()
            clear_screen()

# Ejecutar el programa
if __name__ == "__main__":
    inventario_de_productos()
