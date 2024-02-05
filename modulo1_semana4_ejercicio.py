# se solicita el nombre validando que no se pueda ingresar algo que no sean caracteres alfabéticos ni se deje vacío el campo
while True: 
    nombre = input("Ingresa tu nombre: ")
    if (nombre == "") or (nombre.isdigit())  : 
        print("Intenta de nuevo, no puedes ingresar números o dejar vacío éste campo")
    else:
        break 

# se solicita el apellido paterno validando que no se pueda ingresar algo que no sean caracteres alfabéticos ni se deje vacío el campo
while True: 
    apellido_paterno = input("Ingresa tu apellido paterno: ")
    if (apellido_paterno == "") or (apellido_paterno.isdigit())  : 
        print("Intenta de nuevo, no puedes ingresar números o dejar vacío éste campo")
    else:
        break 

# se solicita el apellido materno validando que no se pueda ingresar algo que no sean caracteres alfabéticos ni se deje vacío el campo
while True: 
    apellido_materno = input("Ingresa tu apellido materno: ")
    if (apellido_materno == "") or (apellido_materno.isdigit())  : 
        print("Intenta de nuevo, no puedes ingresar números o dejar vacío éste campo")
    else:
        break 

# se solicita la edad validando que no se pueda ingresar algo que no sean caracteres numéricos ni se deje vacío el campo
while True: 
    try:
        edad = int(input("Ingresa tu edad: "))
        if (edad.isalpha())  :
            print("Intenta de nuevo, no puedes ingresar letras, números decimales") 
    except ValueError:
        print("Intenta de nuevo, no puedes ingresar letras, números decimales o dejar vacío éste campo")
    except AttributeError:
        break
    
# se solicita el peso validando que no se pueda ingresar algo que no sean caracteres numéricos ni se deje vacío el campo
while True: 
    try:
        peso = int(input("Ingresa tu peso sin decimales: "))
        if (peso == "") or (peso.isalpha())  :
            print("Intenta de nuevo, no puedes ingresar letras, números decimales o dejar vacío éste campo") 
    except ValueError:
        print("Intenta de nuevo, no puedes ingresar letras, números decimales o dejar vacío éste campo")
    except AttributeError:
        break 

# se solicita la estatura validando que no se pueda ingresar algo que no sean caracteres numéricos ni se deje vacío el campo
while True: 
    try:
        estatura = int(input("Ingresa tu estatura en centímetros: "))
        if (estatura == "") or (estatura.isalpha())  : 
            print("Intenta de nuevo, ingresa tu estatura en centímetros, no puedes ingresar letras o dejar vacío éste campo") 
    except ValueError:
        print("Intenta de nuevo, ingresa tu estatura en centímetros, no puedes ingresar letras o dejar vacío éste campo")
    except AttributeError:
        break 

# se imprimen los datos ingresados por el usuario
print("Éstos son tus datos: ")

# se junta el nombre y los apellidos con la primera letra en mayúscula y el resto en minúscula
print("Nombre: " + nombre.title() + " " + apellido_paterno.title() + " " + apellido_materno.title())
print("Tienes " + str(edad) + " años")
print("Tu peso es de: " + str(peso) + " kilogramos")
print("Tu estatura es de: " + str(estatura) + " centímetros")

# se realiza el cálculo del IMC, , se divide la estatura entre 100 para tener el dato en metros, se redondeando el resultado
IMC = round(peso/(estatura/100)**2)

# se imprime el IMC
print("Tu IMC es: " + str(IMC))