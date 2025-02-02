from pymongo import MongoClient
import json

#CONEXION A MONGO
client = MongoClient("mongodb://localhost:27017/")
db = client["LenguajesProgramacion"]  
lenguajes_collection = db["Lenguaje"]     
tipos_lenguaje_collection = db["TipoLenguaje"]
def cargar_json_en_mongo(archivo_json, coleccion):
    with open(archivo_json, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo) 
        if isinstance(datos, dict) and "lenguajes" in datos:
            coleccion.insert_many(datos["lenguajes"])
        elif isinstance(datos, dict) and "tiposLenguaje" in datos:
            coleccion.insert_many(datos["tiposLenguaje"])
        else:
            print("Formato no reconocido en:", archivo_json)          
 #busqueda por id           
def buscar_por_id(id_busqueda):
    lenguaje = lenguajes_collection.find_one({"id": id_busqueda})
    tipo_lenguaje = tipos_lenguaje_collection.find_one({"id": id_busqueda})    
    if lenguaje:
        print("Resultado en colección 'lenguajes':")
        print(lenguaje)
    else:
        print(f"No se encontró un lenguaje con ID {id_busqueda} en la colección 'lenguajes'.")
    if tipo_lenguaje:
        print("\nResultado en colección 'tipos_lenguaje':")
        print(tipo_lenguaje)
    else:
        print(f"No se encontró un tipo de lenguaje con ID {id_busqueda} en la colección 'tipos_lenguaje'.")    
def actualizar_por_id(id_actualizar):
    print("\nActualización en colección 'lenguajes':")
    nuevo_nombre = input("Ingresa el nuevo nombre del lenguaje (o presiona Enter para omitir): ")
    nuevo_creador = input("Ingresa el nuevo creador del lenguaje (o presiona Enter para omitir): ")
    nuevos_datos = {}
    if nuevo_nombre:
        nuevos_datos["nombre"] = nuevo_nombre
    if nuevo_creador:
        nuevos_datos["creador"] = nuevo_creador
    if nuevos_datos:
        lenguajes_collection.update_one({"id": id_actualizar}, {"$set": nuevos_datos})
        print("Actualización completada en colección 'lenguajes'.")
    else:
        print("No se realizaron cambios en colección 'lenguajes'.")

    print("\nActualización en colección 'tipos_lenguaje':")
    nuevo_tipo = input("Ingresa el nuevo tipo de lenguaje (o presiona Enter para omitir): ")
    if nuevo_tipo:
        tipos_lenguaje_collection.update_one({"id": id_actualizar}, {"$set": {"tipo": nuevo_tipo}})
        print("Actualización completada en colección 'tipos_lenguaje'.")
    else:
        print("No se realizaron cambios en colección 'tipos_lenguaje'.")

def eliminar_por_id(id_eliminar):
    resultado1 = lenguajes_collection.delete_one({"id": id_eliminar})
    resultado2 = tipos_lenguaje_collection.delete_one({"id": id_eliminar}) 
    if resultado1.deleted_count > 0:
        print(f"Registro con ID {id_eliminar} eliminado de la colección 'lenguajes'.")
    else:
        print(f"No se encontró un registro con ID {id_eliminar} en la colección 'lenguajes'.")  
    if resultado2.deleted_count > 0:
        print(f"Registro con ID {id_eliminar} eliminado de la colección 'tipos_lenguaje'.")
    else:
        print(f"No se encontró un registro con ID {id_eliminar} en la colección 'tipos_lenguaje'.")

#MENU 
def menu():
    while True:
        print("\nMenú:")
        print("1. Buscar por ID")
        print("2. Actualizar por ID")
        print("3. Eliminar por ID")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            id_busqueda = int(input("Ingresa el ID que deseas buscar: "))
            buscar_por_id(id_busqueda)
        elif opcion == "2":
            id_actualizar = int(input("Ingresa el ID que deseas actualizar: "))
            actualizar_por_id(id_actualizar)
        elif opcion == "3":
            id_eliminar = int(input("Ingresa el ID que deseas eliminar: "))
            eliminar_por_id(id_eliminar)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

menu()
