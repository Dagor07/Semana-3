# ----------------------------
# 📦 1. MÓDULO math
# ----------------------------
import math

print("Raíz cuadrada de 16:", math.sqrt(16))
print("Valor de PI:", math.pi)
print("Redondeo hacia arriba de 3.1:", math.ceil(3.1))
print("Redondeo hacia abajo de 3.9:", math.floor(3.9))

# ----------------------------
# 🎲 2. MÓDULO random
# ----------------------------
import random

print("Número aleatorio entre 1 y 10:", random.randint(1, 10))
print("Elemento aleatorio de ['a', 'b', 'c']:", random.choice(['a', 'b', 'c']))
print("Lista mezclada:", random.sample([1, 2, 3, 4, 5], 3))

# ----------------------------
# 📅 3. MÓDULO datetime
# ----------------------------
import datetime

hoy = datetime.date.today()
print("Fecha actual:", hoy)

ahora = datetime.datetime.now()
print("Fecha y hora actual:", ahora)

# ----------------------------
# 📊 4. MÓDULO statistics
# ----------------------------
import statistics

datos = [10, 20, 30, 40, 50]
print("Promedio:", statistics.mean(datos))
print("Mediana:", statistics.median(datos))
print("Desviación estándar:", statistics.stdev(datos))

# ----------------------------
# 📁 5. MÓDULO os
# ----------------------------
import os

print("Directorio actual:", os.getcwd())
print("Archivos en este directorio:", os.listdir("."))

# ----------------------------
# 💻 6. MÓDULO sys
# ----------------------------
import sys

print("Versión de Python:", sys.version)

# ----------------------------
# 🔐 7. MÓDULO hashlib
# ----------------------------
import hashlib

texto = "hola mundo".encode()
hash = hashlib.sha256(texto).hexdigest()
print("Hash SHA-256 de 'hola mundo':", hash)

# ----------------------------
# 🕒 8. MÓDULO time
# ----------------------------
import time

print("Esperando 2 segundos...")
time.sleep(2)
print("¡Listo!")
