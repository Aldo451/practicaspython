# ejemplos de la función print

# print("hola mundo")
# print("hola mundo", "otra vez")
# print("son las", 9, "de la mañana")
# print("el resultado de 3*4 es:", 3*4)

# ejemplos de cadenas formateadas
# print("el número 15 en sistema decimal es %d, en sistema octal es %o, en sistema hexadecimal es %x" % (15,15,15))

# pi = 3.141592
# r = 5 
# print(f"el radio de un círculo es {r} y el área de ése círculo es {pi * r ** 2: .2f}") # : para indicar que se le va a dar un formato específico, .2 para indicarle cuántos decimales y f para el tipo de formato

# impresión de caracteres especiales
# print("la letra beta es: \n\t \u03B2")

# n = interlineado
# t = tabulación (por default es 4 espacios)

# caracteres de escape , por defecto el caracter de escape es un interlineado entre impresiones
print("hola mundo", end = " ")
print("otra vez", end = "\t")
print("y otra vez")