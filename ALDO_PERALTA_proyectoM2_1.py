# ciclo while para repetir el ciclo hasta que se cumpla la condición buscada
while True:
    entrada = input('Ingresa una palaba de entre 4 y 8 letras: ')

# se declara variable para contar el número de caracteres de la palabra
    longitud = len(entrada)

# condición a cumplir y mensaje de salida: correcto
    if len(entrada) >=4 and len(entrada) <=8:
        print('Palabra correcta!')

# si se cumple la condición se rompe el ciclo
        break

# condición no cumplida caso 1 y mensaje de salida: vuelve a intentar
    elif len(entrada) <4:
        print(f'Hacen falta letras, sólo tiene {longitud} letras')

# condición no cumplida caso 2 y mensaje de salida: vuelve a intentar, debido a que no hay otra opción mas que números \
        # con más de 8 carácteres se usa else en vez de elif.
    else:
        print(f'Sobran letras, tiene {longitud} letras')
    




