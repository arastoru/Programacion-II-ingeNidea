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
