import sqlite3

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect('recetario.db')
cursor = conn.cursor()

# Crear la tabla de recetas si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS recetas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    ingredientes TEXT NOT NULL,
    pasos TEXT NOT NULL
)
''')
conn.commit()


# Función para agregar una receta
def agregar_receta():
    nombre = input("Ingrese el nombre de la receta: ")
    ingredientes = input("Ingrese los ingredientes (separados por comas): ")
    pasos = input("Ingrese los pasos: ")
    cursor.execute("INSERT INTO recetas (nombre, ingredientes, pasos) VALUES (?, ?, ?)", (nombre, ingredientes, pasos))
    conn.commit()
    print("Receta agregada exitosamente.\n")


# Función para actualizar una receta
def actualizar_receta():
    id_receta = input("Ingrese el ID de la receta a actualizar: ")
    nombre = input("Ingrese el nuevo nombre de la receta: ")
    ingredientes = input("Ingrese los nuevos ingredientes (separados por comas): ")
    pasos = input("Ingrese los nuevos pasos: ")
    cursor.execute("UPDATE recetas SET nombre = ?, ingredientes = ?, pasos = ? WHERE id = ?",
                   (nombre, ingredientes, pasos, id_receta))
    conn.commit()
    print("Receta actualizada exitosamente.\n")


# Función para eliminar una receta
def eliminar_receta():
    id_receta = input("Ingrese el ID de la receta a eliminar: ")
    cursor.execute("DELETE FROM recetas WHERE id = ?", (id_receta,))
    conn.commit()
    print("Receta eliminada exitosamente.\n")


# Función para ver todas las recetas
def ver_recetas():
    cursor.execute("SELECT id, nombre FROM recetas")
    recetas = cursor.fetchall()
    print("\nListado de recetas:")
    for receta in recetas:
        print(f"{receta[0]} - {receta[1]}")
    print()


# Función para buscar los ingredientes y pasos de una receta
def buscar_receta():
    id_receta = input("Ingrese el ID de la receta que desea buscar: ")
    cursor.execute("SELECT nombre, ingredientes, pasos FROM recetas WHERE id = ?", (id_receta,))
    receta = cursor.fetchone()
    if receta:
        print(f"\nReceta: {receta[0]}\nIngredientes: {receta[1]}\nPasos: {receta[2]}\n")
    else:
        print("Receta no encontrada.\n")


# Función para mostrar el menú
def mostrar_menu():
    print("Seleccione una opción:")
    print("a) Agregar nueva receta")
    print("b) Actualizar receta existente")
    print("c) Eliminar receta existente")
    print("d) Ver listado de recetas")
    print("e) Buscar ingredientes y pasos de receta")
    print("f) Salir")


# Función principal para ejecutar el programa
def main():
    while True:
        mostrar_menu()
        opcion = input("Opción: ").lower()

        if opcion == 'a':
            agregar_receta()
        elif opcion == 'b':
            actualizar_receta()
        elif opcion == 'c':
            eliminar_receta()
        elif opcion == 'd':
            ver_recetas()
        elif opcion == 'e':
            buscar_receta()
        elif opcion == 'f':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")


# Ejecutar el programa
main()

# Cerrar la conexión a la base de datos al salir
conn.close()
