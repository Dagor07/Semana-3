
# Funciones Avanzadas en Python

Este proyecto contiene una colección de funciones diseñadas para desarrollar lógica más avanzada en Python, así como pruebas automatizadas usando `pytest`.

## Archivos incluidos

- `advance_functions.py`: Contiene 5 funciones útiles aplicadas a casos de uso reales como carrito de compras, análisis de texto, generación de contraseñas, entre otros.
- `testing.py`: Contiene pruebas unitarias para verificar el funcionamiento de cada función.

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

## Descripción de las funciones

### 1. `calcular_total_carrito(productos, iva=0.21)`
Calcula el total a pagar en un carrito con IVA incluido.

### 2. `contar_palabras(texto)`
Devuelve un diccionario con el conteo de cada palabra en un texto, ignorando mayúsculas y signos.

### 3. `generar_contraseña(longitud=12)`
Genera una contraseña segura con letras, números y símbolos.

### 4. `analizar_temperaturas(temperaturas)`
Devuelve el promedio, la temperatura máxima y mínima de una lista de valores.

### 5. Funciones de agenda (`agregar_contacto`, `buscar_contacto`, `eliminar_contacto`)
Permiten manipular una agenda simple de contactos.

---

¡Ideal para practicar funciones puras y mejorar la comprensión de pruebas unitarias!
