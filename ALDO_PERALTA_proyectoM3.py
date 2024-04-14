# se importan las librerias a utilizar
import numpy as np
import random
import matplotlib.pyplot as plt

# función para calcular el trayecto que va a llevar las canicas a través de los niveles
def simulacion(canicas,niveles):
# se crea una lista con valor 0 para ir agregando los resultados de las iteracciones
    resultados= np.zeros(niveles)
# ciclo para las canicas    
    for i in range (canicas):
# punto central desde donde van a iniciar el trayecto las canicas
        inicio = 0
# ciclo para los niveles que tienen que cruzar cada una de las canicas        
        for j in range (niveles):
# se genera un número aleatorio (0 o 1)
            lado = np.random.randint(0,2)
# si el valor generado es 0 la canica se va a mover a la izquierda            
            if lado == 1:
                inicio += 1
# el resultado de la canica después de los 12 niveles se va a ir guardando en una lista        
        resultados[inicio]+=1
# la función devuelve la lista     
    return resultados

# función para graficar el resultado en donde terminan las canicas
def grafica(resultados):
# se establecen los valores para las etiquetas, título, color y valores
    plt.bar(range(len(resultados)),resultados, color='g')
    plt.xlabel('distribución de canicas')
    plt.ylabel('canicas')
    plt.title('Simulación de máquina de Galton')
    plt.show()

# se definen los valores de las variables a utilizar
canicas = 3000
niveles = 12

# se llama a la función que calcula el trayecto de las canicas
resultado=simulacion(canicas,niveles)

# se llama a la fuinción para graficar el resutlado obtenido en la función anterior
grafica(resultado)
