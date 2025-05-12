# 1. strip
texto1 = "   hola   "
print("strip:", texto1.strip())  # "hola"

# 2. lstrip y rstrip
texto2 = "   hola   "
print("lstrip:", texto2.lstrip())  # "hola   "
print("rstrip:", texto2.rstrip())  # "   hola"

# 3. lower y upper
texto3 = "HoLa"
print("lower:", texto3.lower())  # "hola"
print("upper:", texto3.upper())  # "HOLA"

# 4. capitalize
texto4 = "hola mundo"
print("capitalize:", texto4.capitalize())  # "Hola mundo"

# 5. title
texto5 = "hola mundo"
print("title:", texto5.title())  # "Hola Mundo"

# 6. replace
texto6 = "hola mundo"
print("replace:", texto6.replace("hola", "hello"))  # "hello mundo"

# 7. split
texto7 = "uno,dos,tres"
print("split:", texto7.split(","))  # ['uno', 'dos', 'tres']

# 8. join
lista = ["uno", "dos", "tres"]
print("join:", "-".join(lista))  # "uno-dos-tres"

# 9. startswith y endswith
texto9 = "python"
print("startswith:", texto9.startswith("py"))  # True
print("endswith:", texto9.endswith("on"))     # True

# 10. find e index
texto10 = "hola mundo"
print("find:", texto10.find("mundo"))   # 5
print("find (no encontrado):", texto10.find("x"))  # -1
# print("index:", texto10.index("x"))  # Esto lanza un error si no existe

# 11. isdigit e isalpha
texto11a = "123"
texto11b = "abc"
print("isdigit:", texto11a.isdigit())  # True
print("isalpha:", texto11b.isalpha())  # True

# 12. strip con caracteres específicos
texto12 = "$$$hola$$$"
print("strip con '$':", texto12.strip("$"))  # "hola"
