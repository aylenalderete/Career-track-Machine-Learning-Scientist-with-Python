#Abrir archivos usando Python base.
#Para hacerlo usaremos la sentencia with para definir un contexto del siguiente modo:

with open('corpus.txt', 'r') as inp:
    string_contenido = inp.read()

# Lo que significa: con el archivo "corpus.txt" abierto en modo lectura ("r" de read) con el alias inp,
# definimos la variable contenido usando el método .read() para leer el archivo. Algunas aclaraciones:

# El método .read() es propio del objeto de input, que en esta ocasión llamamos inp. Otro método útil es .readlines() que nos permite iterar por renglones.
# La ruta al archivo puede ser relativa como en este caso, donde el archivo se encontraría en la misma carpeta que la notebook. También se puede dar el path completo, como podría ser "C:/Usuarios/Matías/Documentos/corpus.txt"
# Existen varios modos de abrir un archivo, incluyendo:

# - r: read, lectura
# - w: write, escritura
# - a: append, agregar al final del archivo
# Por ejemplo, para escribir en un archivo, haríamos:

with open(outpath, 'w') as f:
    f.write(string)

with open('nuevo.txt', 'w') as f:
    f.write('ejemplo de escritura')
    

with open('nuevo.txt', 'r') as f:
    contenido = f.read()
print(contenido)


while True:
    usuario_dijo = input('Ingrese un numero')
    try:
        num = int(usuario_dijo)
        break
    except:
        print('No anduvo, intente de nuevo')
print(f'Su numero fue {num}! :D')