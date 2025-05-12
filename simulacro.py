# Sistema de gestión de inventario para una librería

# Lista inicial de libros (cada libro es un diccionario)
inventario = [
    {"titulo": "Libro 1", "precio": 10.0, "cantidad": 100},
    {"titulo": "Libro 2", "precio": 15.0, "cantidad": 50},
    {"titulo": "Libro 3", "precio": 20.0, "cantidad": 30},
    {"titulo": "Libro 4", "precio": 25.0, "cantidad": 10},
    {"titulo": "Libro 5", "precio": 30.0, "cantidad": 5}
]

# Función para agregar un nuevo libro al inventario
def agregar_libro():
    titulo = input("Ingrese el título del libro: ").strip()
    try:
        precio = float(input("Ingrese el precio del libro: "))
        cantidad = int(input("Ingrese la cantidad disponible: "))
        if precio <= 0 or cantidad < 0:
            print("El precio debe ser positivo y la cantidad no puede ser negativa.")
            return
        inventario.append({"titulo": titulo, "precio": precio, "cantidad": cantidad})
        print(f"Libro '{titulo}' agregado correctamente.")
    except ValueError:
        print("Entrada no válida. El precio debe ser un número y la cantidad un entero.")

# Función para buscar un libro por título
def consultar_libro():
    titulo = input("Ingrese el título del libro a consultar: ").strip()
    for libro in inventario:
        if libro["titulo"].lower() == titulo.lower():
            print(f"Título: {libro['titulo']}, Precio: ${libro['precio']:.2f}, Cantidad: {libro['cantidad']}")
            return
    print(f"El libro '{titulo}' no se encuentra en el inventario.")

# Función para actualizar el precio de un libro
def actualizar_precio():
    titulo = input("Ingrese el título del libro a actualizar: ").strip()
    for libro in inventario:
        if libro["titulo"].lower() == titulo.lower():
            try:
                nuevo_precio = float(input("Ingrese el nuevo precio: "))
                if nuevo_precio <= 0:
                    print("El precio debe ser un número positivo.")
                    return
                libro["precio"] = nuevo_precio
                print(f"Precio del libro '{titulo}' actualizado correctamente.")
                return
            except ValueError:
                print("Precio no válido. Debe ser un número.")
                return
    print(f"El libro '{titulo}' no existe en el inventario.")

# Función para eliminar un libro del inventario
def eliminar_libro():
    titulo = input("Ingrese el título del libro a eliminar: ").strip()
    for libro in inventario:
        if libro["titulo"].lower() == titulo.lower():
            inventario.remove(libro)
            print(f"Libro '{titulo}' eliminado del inventario.")
            return
    print(f"El libro '{titulo}' no existe en el inventario.")

# Función para calcular el valor total del inventario
def calcular_valor_total():
    total = sum(libro["precio"] * libro["cantidad"] for libro in inventario)
    print(f"Valor total del inventario: ${total:.2f}")

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\n--- Gestión de Inventario de la Librería ---")
    print("1. Agregar un nuevo libro")
    print("2. Consultar un libro")
    print("3. Actualizar precio de un libro")
    print("4. Eliminar un libro")
    print("5. Calcular valor total del inventario")
    print("6. Salir")

# Bucle principal del programa
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ").strip()
        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            consultar_libro()
        elif opcion == "3":
            actualizar_precio()
        elif opcion == "4":
            eliminar_libro()
        elif opcion == "5":
            calcular_valor_total()
        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor seleccione un número del 1 al 6.")

# Ejecutar el programa
main()
