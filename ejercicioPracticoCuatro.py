# Ejercicio pŕactico número cuatro

blank = ""
error_msg = "ERROR!"

name = input("A continuación ingrese su nombre: ")
lastName = input("A continuación ingrese su apellido: ")
age = int(input("A continuación ingrese su edad: "))
email = input("A continuación ingrese su dirección de email: ")

# --- Formateo de nombre y apellido ---
name = name.strip().title()       # Convierte a formato Nombre
lastName = lastName.strip().title()  # Convierte a formato Apellido

# --- Limpieza y validación del email ---
email = email.strip()  # Elimina espacios en los extremos
valid_email = email.count("@") == 1  # Verifica que tenga exactamente un '@'

# --- Clasificación etaria ---
if age < 15:
    category = "Niño/a"
elif 15 <= age <= 18:
    category = "Adolescente"
else:
    category = "Adulto/a"

# --- Validación de todos los datos ---
if name == blank or lastName == blank or not valid_email or age <= 0:
    print(error_msg)
else:
    print(f"""
Los datos ingresados son:
- Nombre y Apellido: {name} {lastName}
- Edad: {age} años ({category})
- Email: {email}
""")