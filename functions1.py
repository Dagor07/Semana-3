from datetime import date

# 1. 💰 Calculadora de propina  
def calculate_tip(value, percentage):
    return value * percentage / 100

# 2. 📏 Conversor de unidades  
def meters_to_kilometers(meters):
    return meters / 1000

# 3. ✉️ Generador de email empresarial 
def create_email(name, lastname, domain):
    return f"{name.lower()}.{lastname.lower()}@{domain.lower()}"

# 4. 🧾 Precio con impuestos  
def final_price(base_price, iva=0.21):
    return base_price + (iva * 100)

# 5. 🔐 Simulador de login  
def validate_login(username, password):
    if username == "admin" and password == "1234":
        print("Inicio de sesión exitoso")
        return True

    print("Credenciales incorrectas")
    return False

# 6. 🧑‍💻 Generador de nombre de usuario
def generate_username(name, birthday):
    str_birtday = str(birthday)
    return f"{name.lower()}{str_birtday[2:]}"


# 7. ✨ Formateador de nombres  
def format_name(fullname: str):
    name, lastname = fullname.split(" ")
    # fullname.title()
    return f"{name.capitalize()} {lastname.capitalize()}"

# 8. 🎂 Calculadora de edad
def calculate_age(birthdate):
    return date.today().year - birthdate

# 9. 📞 Validación de número telefónico  
def validate_phone(number):
    phone = str(number)
    if not phone.isnumeric() or len(phone) != 10:
        return False
    return True

# 10. 🧠 Notas de estudiantes
def student_average(name, *notes):
    average = sum(notes) / len(notes)
    print(f"{name}: Promedio = {average:.2f}")
    return average