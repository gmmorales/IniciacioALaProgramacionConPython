# Ejercicio pŕactico número tres

blank = ""
error_msg = "ERROR!"
space = " "

name = input("A continuación ingresé su nombre: ")
lastName = input("A continuación ingresé su apellido: ")
age = int(input("A continuación ingresé su edad:"))
email = input("A continuación ingresé dirección de email: ")


# Implementación de la validación de los datos: nombre, apellido y mail
if name == blank or lastName == blank or email == blank or age <= 18:
    print(error_msg)
else:
    print("Los datos ingresado son: " + name + space + lastName + space + str(age) + space + email)
