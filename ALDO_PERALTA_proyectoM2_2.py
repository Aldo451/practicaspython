print('Ingresa las coordenadas de un punto en el plano cartesiano: ')
# se hace la validación para que no se puedan 0 como valor
while True:    
    x = int(input('Ingresa el valor de X: '))
    if x==0:
        print('El valor de x no puede ser 0, intenta de nuevo')
    else:
        break

# se hace la validación para que no se puedan 0 como valor
while True:
    y = int(input('Ingresa el valor de Y: '))
    if y==0:
        print('El valor de y no puede ser 0, intenta de nuevo')
    else:
        break

# de acuerdo a los valores de x y y se determina que tipo de cuadrante correspondería
    #NOTA: desde aquí se podría devolver el resultado del cuadrante al que pertence pero se optó por éste método para hacer uso de un diccionario
if x>0 and y>0:
    resultado ='caso_1'
elif x<0 and y>0:
    resultado = 'caso_2'
elif x<0 and y<0:
    resultado = 'caso_3'
elif x>0 and y<0:
    resultado = 'caso_4'

# se crea el diccionario para identificar el cuadrante correspondiente a partir del tipo de cuadrante correspondiente
cuadrante = {'caso_1':'I', 'caso_2':'II', 'caso_3':'III', 'caso_4':'IV'}

# a partir del caso que representan los datos ingresados por el usuario se devuelve el cuadrante al que pertenecen las coordenadas
for resultado in resultado: 

# si el resultado se encuentra dentro del diccionario
    if resultado in cuadrante:

# devuelve el valor de la llave dentro del diccionario
        resultado = cuadrante[resultado]

# se imprime el resultado para el usuario 
print(f'El punto se encuentra en el cuadrante {resultado}')


