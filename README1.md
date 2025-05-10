# 🐍 Ejercicios prácticos con funciones en Python

Esta colección incluye 10 ejercicios prácticos. Cada ejercicio se enfoca en escribir funciones simples pero útiles para reforzar el uso de parámetros, retornos y lógica básica.

##  Archivos incluidos

- ```testing.py```: Contiene pruebas unitarias para verificar el funcionamiento de cada función

## Requisitos

- Python 3.8+
- `pytest` instalado (puedes instalarlo con `pip install pytest`)

## Cómo ejecutar las pruebas

1. Clona este repositorio o descarga los archivos.
2. Abre la terminal y navega a la carpeta donde se encuentran los archivos.
3. Ejecuta el siguiente comando:

```bash
pytest testing.py
```

## 🚀 Ejercicios

### 1. 💰 Calculadora de propina  
**Función:** `calculate_tip(monto, porcentaje)`  
**Descripción:** Devuelve la propina que se debe dejar en un restaurante.

---

### 2. 📏 Conversor de unidades  
**Función:** `meters_to_kilometers(metros)`  
**Descripción:** Convierte una distancia en metros a kilómetros.

---

### 3. ✉️ Generador de email empresarial  
**Función:** `create_email(nombre, apellido, dominio)`  
**Descripción:** Genera un correo con el formato `nombre.apellido@dominio`.

---

### 4. 🧾 Precio con impuestos  
**Función:** `final_price(precio_base, iva=0.21)`  
**Descripción:** Devuelve el precio total incluyendo el IVA (por defecto 21%).

---

### 5. 🔐 Simulador de login  
**Función:** `validate_login(usuario, contraseña)`  
**Descripción:** Verifica si las credenciales coinciden con un usuario registrado (datos hardcodeados).

---

### 6. 🧑‍💻 Generador de nombre de usuario  
**Función:** `generate_username(nombre, nacimiento)`  
**Descripción:** Devuelve un nombre de usuario del tipo `nombreYY`. Ejemplo: `lucas97`.

---

### 7. ✨ Formateador de nombres  
**Función:** `format_name(nombre_completo)`  
**Descripción:** Formatea el nombre completo a formato título. Ejemplo: `juan perez` → `Juan Perez`.

---

### 8. 🎂 Calculadora de edad  
**Función:** `calculate_age(año_nacimiento)`  
**Descripción:** Devuelve la edad actual de una persona según el año de nacimiento.

---

### 9. 📞 Validación de número telefónico  
**Función:** `validate_phone(numero)`  
**Descripción:** Retorna `True` si el número tiene exactamente 10 dígitos.

---

### 10. 🧠 Notas de estudiantes  
**Función:** `student_average(nombre, *notas)`  
**Descripción:** Imprime el nombre del estudiante y su promedio con 2 decimales.

---

¡Feliz práctica! 🚀
