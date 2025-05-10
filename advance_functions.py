import string
import random

# 1. Shopping cart simulator
def calculate_cart_total(cart: dict, iva: float = 0.21) :
    total = 0
    for product in cart:
        total += product["price"] * product["quantity"]
    return total + (total * iva)

# 2. Text processing (word count)
def word_count(text: str):
    tbl_translate = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(tbl_translate)
    count = {}
    for text in clean_text.split(" "):
        text = text.lower()
        if text in count:
            count[text] += 1
            continue
        count[text] = 1
    return count

# 3. Secure password generator
def generate_password(length: int = 12):
    letters = "abcdefghijklmnopqrstuvwxyz.*',#&$"
    letters_length = len(letters)
    password = ""
    for _ in range(length):
        password += letters[random.randint(0, letters_length-1)]
    return password

# 4. Weather analyzer (temperatures)
def analyze_temperatures(temps: list):
    max_t = 0
    min_t = 99999
    sum = 0
    for temp in temps:
        if temp > max_t:
            max_t = temp
        if temp < min_t:
            min_t = temp
        sum += temp
    avg = sum / len(temps)
    return avg, max_t, min_t

# 5. Functional contact book
def add_contact(book: dict, name: str, password: str):
    book[name] = password
    return book

def find_contact(book: dict, name: str):
    return str(book[name])

def delete_contact(book: dict, name: str):
    book[name] = "No encontrado"
    return book