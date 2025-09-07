# Ejercicio pŕactico número cinco

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

# --- Ingresos mensuales durante los próximos seis meses ---
current_month = 1
final_month = 7
accumulated_income = 0

while current_month < final_month:
    income = int(input("Ingreso mensual del mes " + str(current_month) + ": "))
    
    # Validar que no sea negativo
    while income < 0:
        print("Valor ingresado no válido. Vuelve a intentar.")
        income = int(input("Ingreso mensual del mes " + str(current_month) + ": "))
    
    accumulated_income += income
    print("Acumulado hasta el mes", current_month, ":", accumulated_income)
    
    current_month += 1  # ¡Avanzar al siguiente mes!

print("\n✅ El ingreso total acumulado en 6 meses es:", accumulated_income)


# --- Validación de todos los datos ---
if name == blank or lastName == blank or not valid_email or age <= 0:
    print(error_msg)
else:
    print(f"""
Los datos ingresados son:
- Nombre y Apellido: {name} {lastName}
- Edad: {age} años ({category})
- Email: {email}
- Total acumulado por seis meses: {accumulated_income}
""")