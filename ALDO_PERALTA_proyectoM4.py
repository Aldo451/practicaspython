# se importan las librerías necesarias:

# requests para hacer las peticiones a la API
import requests
# matplotlib.pyplot, PIL/Image para poder mostrar la imágen del Pokémon
import matplotlib.pyplot as plt
from PIL import Image
# urllib.request para poder abrir la url que contiene la imágen del Pokémon
from urllib.request import urlopen

# se solicita al usuario que introduzca el nombre del Pokémon a consultar
pokemon = input('Pon un Pokémon: ')

# se indica la url la cual termina con el nombre del Pokémon por lo que se agrega la variable al final
url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon

# se hace la petición a la url indicada anteriormente
respuesta = requests.get(url)

# si al hacer la petición la API devuelve algo distinto a 200 (proceso exitoso) manda un mensaje de error y finaliza el programa
if respuesta.status_code != 200:
     print('Pokémon no encontrado')
     exit()

# se pasan los datos recuperados de la API a un archivo json para poder consultar datos específicos
datos = respuesta.json()

# se abre un ciclo try/except para que en caso de que el Pokémon no tenga imágen mande un mensaje notificándolo
try:
     # se define que la url de la imágen se encuentra en el primer elemento 'sprites' y dentro del elemento hijo 'front_default'
     url_imagen = datos['sprites']['front_default']
     # se define al elemento imágen a través de la librería Image y abriendo la url
     imagen = Image.open(urlopen(url_imagen))
except:
     print('El Pokémon no tiene imágen')

# dentro de la imágen a mostrar se coloca el nombre del Pokémon como si fuera el título de un gráfico y se muestra la imágen obtenida
plt.title(datos['name'])
imgplot = plt.imshow(imagen)
plt.show()

# se guardan los datos deseados como variables
nombre = datos['name']
peso = datos['weight']
tamaño = datos['height']

# se imprimen en la terminal las variables con los datos deseados 
print('Datos del Pokémon:')
print(f'Nombre: {nombre}')
print(f'Peso: {peso}')
print(f'Tamaño: {tamaño}')
print('Movimientos:')


# se crea una variable con la ruta a seguir
f_archivo_carpeta='E:\\Users\\aperalfi\\Documents\\Curso Python\\Pokedex\\Datos_Pokémon.txt'

# se abre el archivo buscando la variable de la ruta
f_archivo = open(f_archivo_carpeta,'w')

# se escribenen el txt los datos y variables ya definidas
f_archivo.write('Datos del Pokémon:')
f_archivo.write('\n'f'Nombre: {nombre}')
f_archivo.write('\n'f'Peso: {peso}')
f_archivo.write('\n'f'Tamaño: {tamaño}')
f_archivo.write('\nMovimientos:')

# se cierra el archivo para continuar con el programa
f_archivo.close()

# debido a que el Pokémon tiene una lista de movimientos lo que se hace es iterar sobre los elementos que se encuentran dentro de 'moves'
movimientos = datos['moves']
# se obtienen el número de movimientos que posee el Pokémon con len()
# ése dato se convierte a un número entero con int() para poder convertirlo a un rango con range() sobre el cual se va a poder iterar
for i in range(int(len(movimientos))):
     # se indica que la variable 'movimiento' es el el emento contenido en el número de variable [i] y se solicita la información del elemento 'name' que está contenido en el elemento 'move'
     movimiento=movimientos[i]['move']['name']
     # se imprime la lista de movimientos. La impresión tiene que estar dentro del ciclo for para poder imprimir el resultado de las iteraciones
     print(f'- {movimiento}')


     # dentro del ciclo for se abre el archivo para ingresar através del modo 'a' (append) el listado definido dentro del ciclo 
     with open(f_archivo_carpeta,'a') as f_archivo:
          f_archivo.write('\n'f'- {movimiento}')



# debido a que el Pokémon tambien tiene mas de una habilidad se repite el proceso realizado para los movimientos
print('Habilidades:')

#  se abre el archivo para ingresar como texto el apartado de Habilidades
with open(f_archivo_carpeta,'a') as f_archivo:
     f_archivo.write('\nHabilidades:')

habilidades = datos['abilities']
for i in range(int(len(habilidades))):
     habilidad=habilidades[i]['ability']['name']
     print(f'- {habilidad}')
     

     # se repite el proceso realizado en los movimientos para el append de las habilidades
     with open(f_archivo_carpeta,'a') as f_archivo:
          f_archivo.write('\n'f'- {habilidad}')

#  se abre el archivo para ingresar como texto el apartado de Tipos
with open(f_archivo_carpeta,'a') as f_archivo:
     f_archivo.write('\nTipos:')

# lo mismo para los tipos ya que no conocemos si el Pokémon tiene mas de 1 tipo (subtipos)
tipos = datos['types']
for i in range(int(len(tipos))):
     tipo=tipos[i]['type']['name']
     print(f'Tipos: {tipo}')


     # se repite el proceso realizado en los movimientos para el append de los tipos
     with open(f_archivo_carpeta,'a') as f_archivo:
          f_archivo.write('\n'f'- {tipo}')

# por último se guarda el link de la imágen del Pokémon como una cadena dentro del archivo a través de un append
with open(f_archivo_carpeta,'a') as f_archivo:
     f_archivo.write('\n'f'URL de la imágen: {url_imagen}')
