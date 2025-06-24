#Diccionario cancion
cancion = {
  "titulo": "Yellow",
  "artista": "Coldplay",
  "album": "Parachutes",
  "duracion_segundos": 266,
  "genero": "Alternative Rock",
  "fecha_lanzamiento": "2000-06-26"
}
print("Información de la canción")
print(f"Título: {cancion['titulo']}")
print(f"Artista: {cancion['artista']}")
print(f"Álbum: {cancion['album']}")
print(f"Duración: {cancion['duracion_segundos']} segundos")
print(f"Género: {cancion['genero']}")
print(f"Fecha de lanzamiento: {cancion['fecha_lanzamiento']}")
#Diccionario post red social
post_red_social = {
    "id_post": "P0ST001",
    "autor": "Franz123",
    "contenido_texto": "¡Qué gran día para aprender sobre diccionarios en Python! #Python #Programación #Aprendiendo",
    "lista_de_likes": ["Usuario1", "Usuario2", "Usuario3", "UsuarioEjemplo123"],
    "fecha_publicacion": "2025-06-24 08:45:00"
}

print("Información del Post de Red Social")
print(f"ID del Post: {post_red_social['id_post']}")
print(f"Autor: {post_red_social['autor']}")
print(f"Contenido: {post_red_social['contenido_texto']}")
print(f"Likes: {', '.join(post_red_social['lista_de_likes'])}") 
print(f"Fecha de Publicación: {post_red_social['fecha_publicacion']}")


#  Codigo Inventario
# 1. Crear una lista vacía llamada inventario
inventario = []

# 2. Crear al menos tres diccionarios de productos diferentes
producto1 = {
    "nombre": "Chocolate para Taza 'El Ceibo'",
    "stock": 50
}

producto2 = {
    "nombre": "Café de los Yungas",
    "stock": 100
}

producto3 = {
    "nombre": "Quinua Real en Grano",
    "stock": 80
}

# 3. Añadir los productos al inventario
inventario.append(producto1)
inventario.append(producto2)
inventario.append(producto3)

# 4. Imprimir cantidad de tipos de producto
print(f"\nCantidad de productos en inventario: {len(inventario)}")

# 5. Recorrer el inventario e imprimir resumen
print("\n--- Inventario Actual ---")
for producto in inventario:
    print(f"- {producto['nombre']}: {producto['stock']} unidades en stock.")

#Codigo Key, items
#1 Uso de .keys(): Obtener todas las claves

producto = {
  "codigo": "P001",
  "nombre": "Chocolate para Taza 'El Ceibo'",
  "precio_unitario": 15.50,
  "stock": 50,
  "proveedor": "El Ceibo Ltda."
}

# Mostrar todas las claves
print("Claves del diccionario producto:")
for clave in producto.keys():
  print(f"→ {clave}")

#2 Uso de .keys(): Obtener todas las claves
print("\nValores del diccionario producto:")
for valor in producto.values():
    print(f"→ {valor}")

#3 Uso de .items(): Recorrer clave y valor al mismo tiempo (¡muy útil!)

print("\nContenido completo del diccionario producto:")
for clave, valor in producto.items():
    print(f"{clave}: {valor}")

#4 Verificar si una clave existe usando in
clave_a_verificar = "en_oferta"

if clave_a_verificar in producto:
    print(f"\n🔍 La clave '{clave_a_verificar}' existe con valor: {producto[clave_a_verificar]}")
else:
    print(f"\n❌ La clave '{clave_a_verificar}' no existe.")

# Recuerda que también puedes usar not in para verificar si una clave NO existe
# o eitar un KeyError accediendo a una clave solo si existe
if "stock" in producto:
    print(f"Stock disponible: {producto['stock']} unidades")
else:
    print("No hay información de stock.")

#Aplicado al inventario (con .items())
inventario = [
  {"nombre": "Chocolate para Taza 'El Ceibo'", "stock": 50},
  {"nombre": "Café de los Yungas", "stock": 100},
  {"nombre": "Quinua Real en Grano", "stock": 80}
]

print("\n--- Detalle de productos usando .items() ---")
for producto in inventario:
  for clave, valor in producto.items():
      print(f"{clave} → {valor}")
  print("---")

# Modelado de datos con diccionarios para Canción
cancion = {
  "titulo": "Bohemian Rhapsody",
  "artista": "Queen",
  "album": "A Night at the Opera",
  "duracion_segundos": 354,  # (5 minutos 54 segundos)
  "genero": "Rock Progresivo",
  "es_explicita": False,
  "reproducciones": 275_000_000
}
#"duracion_segundos" es un número entero.
#"es_explicita" es un booleano.
#"reproducciones" usa el separador _ para mejor lectura

# Mostrar los datos
print("🎵 Canción:")
for clave, valor in cancion.items():
  print(f"{clave}: {valor}")

# Modelado de datos con diccionarios para Coche
coche = {
  "marca": "Toyota",
  "modelo": "Corolla Cross",
  "año": 2023,
  "color": "Gris Metálico",
  "placa": "5923-LLT",
  "kilometraje": 17450.6,
  "en_venta": True
}
#"kilometraje" es un número decimal.
#"año" es un entero.
#"en_venta" es booleano.

# Mostrar los datos
print("\n🚗 Coche:")
for clave, valor in coche.items():
  print(f"{clave}: {valor}")

# Modelado de datos con diccionarios para Post de Red Social
post_red_social = {
  "id_post": "POST-20250622-001",
  "autor": "jimmy.requena",
  "contenido_texto": "¡Hoy lanzamos nuestro nuevo ERP con IA! 🚀",
  "lista_de_likes": ["ana_123", "dev.mario", "claudia77"],
  "fecha_publicacion": "2025-06-22",
  "es_publico": True,
  "hashtags": ["#IA", "#ERP", "#ProductLaunch"]
}

# Mostrar los datos
print("\n📱 Post en Red Social:")
for clave, valor in post_red_social.items():
  print(f"{clave}: {valor}")
post_red_social = {
  "id_post": "POST-20250622-001",
  "autor": "jimmy.requena",
  "contenido_texto": "¡Hoy lanzamos nuestro nuevo ERP con IA! 🚀",
  "lista_de_likes": ["ana_123", "dev.mario", "claudia77"],
  "fecha_publicacion": "2025-06-22",
  "es_publico": True,
  "hashtags": ["#IA", "#ERP", "#ProductLaunch"]
}
#"lista_de_likes" y "hashtags" son listas de strings.
#"fecha_publicacion" es un string con formato de fecha.
#"es_publico" es booleano.

# Mostrar los datos
print("\n📱 Post en Red Social:")
for clave, valor in post_red_social.items():
  print(f"{clave}: {valor}")

# Probando si existe una clave
if "autor" in post_red_social:
  print(f"\n✅ Autor del post: {post_red_social['autor']}")
else:
  print("❌ Este post no tiene autor definido.")

