#Manejo de strings en Python
#Nombre:César Enrique García Samano
#Matricula: 2630328
#Grupo: M1-1

print("----------------------------------")

#Resumen ejecutivo
#1. ¿Qué es un string en Python?
# Un string (str) es un tipo de dato que permite almacenar texto, como nombres,
# palabras o frases. Se escribe entre comillas simples o dobles. 
#Es inmutable, lo que significa que no se puede modificar directamente su contenido original.

#2. ¿Qué operaciones básicas se pueden realizar?
#Concatenar: unir textos con +. Ejemplo: "Hola" + " mundo".
#Obtener longitud: usar len() para contar los caracteres.
#Extraer subcadenas: usar índices o segmentos para obtener una parte del texto, como "Python"[0:3], que devuelve "Pyt".
# Buscar patrones: usar find() para localizar texto dentro de una cadena.
#Reemplazar texto: usar replace() para cambiar una parte por otra.

#3. ¿Por qué es importante validar y normalizar el texto?
#Es importante para comprobar que los datos sean correctos y tengan un formato uniforme.
#Por ejemplo, validar que un correo tenga un formato adecuado, eliminar espacios 
#innecesarios en nombres y verificar que las contraseñas cumplan ciertos requisitos.
#Esto ayuda a evitar errores y mejora la seguridad de los programas.

print("----------------------------------")

#Problem 1: Full name formatter (name + initials)
print("Problem 1:")

#Description: Create a Python program that formats a full name, removes extra spaces,
#converts it to Title Case, generates initials, and validates the input.

#Validations:
#- full_name must not be empty after strip().
#- Must contain at least two words.
#- Do not accept strings that consist only of spaces.

#Test cases:
# 1) Normal: "juan carlos tovar perez"
# 2) Border: "ana perez" (two words)
# 3) Error: "" or "   " (empty or only spaces)

# Inputs:
full_name = input("Enter full name: ")
 
# Code:
full_name = full_name.strip()
is_valid = True
formatted_name = ""
initials = ""
 
if full_name == "":
    print("Error: The input cannot be empty or contain only spaces.")
    is_valid = False
else:
    words = full_name.split()
 
    if len(words) < 2:
        print("Error: The name is too short (must contain at least two words).")
        is_valid = False
    else:
        formatted_name = " ".join([word.title() for word in words])
        initials = ".".join([word[0].upper() for word in words]) + "."
 
# Output:
if is_valid:
    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")
 
print("----------------------------------")

#Problem 2: Simple email validator (structure + domain)
print("Problem 2:")

#Description:Create a Python program that checks if an email address has a basic valid
#format. It verifies the presence of exactly one '@', a dot after it, and no spaces.
#If the email is valid, the program also displays its domain.

#Validations:
#- email_text must not be empty after strip().
#- Count how many times '@' appears.
#- Verify that there are no blank spaces.

#Test cases:
# 1) Normal: "usuario@gmail.com"
# 2) Border: "a@b.c"
# 3) Error: "usuariogmail.com"

# Inputs:
email_text = input("Enter an email: ")
 
# Code:
email_text = email_text.strip()
valid_email = True
domain_part = ""
 
if email_text == "":
    valid_email = False
elif email_text.count("@") != 1:
    valid_email = False
elif " " in email_text:
    valid_email = False
else:
    at_index = email_text.find("@")
    if "." not in email_text[at_index + 1:]:
        valid_email = False
    else:
        domain_part = email_text[at_index + 1:]
 
# Outputs:
print(f"Valid email: {str(valid_email)}")
 
if valid_email:
    print(f"Domain: {domain_part}")
print("----------------------------------")

# Problem 3: Palindrome checker (ignoring spaces and case)
print("Problem 3:")

#Description:Create a Python program that determines whether a phrase is a palindrome 
#by ignoring spaces and uppercase or lowercase letters. 
#The program displays the normalized phrase and whether it is a palindrome.

#Validations:
#- phrase must not be empty after strip().
#- Minimum reasonable length after clearing spaces (at least 3 characters).

#Test cases:
#1) Normal: "Anita lava la tina"
#2) Border: "Aba"
#3) Error: "Ab" (too short)

#inputs:
phrase = input(" insert phrase: ")

#Code:
phrase_stripped = phrase.strip()
valid_phrase = True
normalized = ""
is_palindrome = False

if phrase_stripped == "":
    print("Error: The input cannot be empty or contain only spaces.")
    valid_phrase = False
else:
    normalized = "".join(phrase_stripped.lower().split())
    
    if len(normalized) < 3:
        print("Error: The phrase is too short (must be at least 3 characters).")
        valid_phrase = False
    else:
        if normalized == normalized[::-1]:
            is_palindrome = True

#Output:
if valid_phrase:
    print(f"Normalized phrase: {normalized}")
    print(f"Is palindrome: {is_palindrome}")

print("----------------------------------")

#Problem 4: Sentence word stats (lengths and first/last word)
print("Problem 4:")

#Description: This practice consists of analyzing a sentence to count its words, 
#identify the first and last words, and find the shortest and longest words. 
#It uses Python string methods such as strip(), split(), and len() to process and validate the input.

#Validations:
#- Sentence must not be empty after strip().
#- Must contain at least one valid word after split().

#Test cases:
#1) Normal: "El perro corre rapido"
#2) Border: "Hola"
#3) Error: "" (empty)

#input
sentence = input("insert sentence:")
 
# Code:
sentence = sentence.strip()
 
if len(sentence) == 0:
    print("Error: The sentence cannot be empty.")
else:
    words = sentence.split()
    n_words = len(words)
 
    longest_word = words[0]
    shortest_word = words[0]
 
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
        if len(word) < len(shortest_word):
            shortest_word = word
 
    # Outputs:
    print(f"Word count: {n_words}")
    print(f"First word: {words[0]}")
    print(f"Last word: {words[-1]}")
    print(f"Longest word: {longest_word}")
    print(f"Shortest word: {shortest_word}")

print("----------------------------------")

#Problem 5: Password strength classifier
print("Problem 5:")

#Description: This practice consists of evaluating a password and classifying 
#its strength as weak, medium, or strong based on its length and the types of characters
#it contains. It also validates that the password is not empty and uses Python
#string methods to check its characteristics.

#Validations:
#- Do not accept an empty password.
#- Verify length using len().

#Test cases:
#1) Normal: "Abc12345#" (strong)
#2) Border: "abcdefgh" (weak/medium)
#3) Error: "" (empty)

#inputs:
password_input = input("Password classifier:")
 
# Code:
password_length = len(password_input)
 
has_upper = False
has_lower = False
has_digit = False
has_symbol = False
password_valid = True
strength = ""
 
if password_length == 0:
    print("Error: The Password cannot be empty.")
    password_valid = False
 
for caracter in password_input:
    if caracter.isupper():
        has_upper = True
    if caracter.islower():
        has_lower = True
    if caracter.isdigit():
        has_digit = True
    if not caracter.isalnum():
        has_symbol = True
 
if password_length >= 8 and has_upper and has_lower and has_digit and has_symbol:
    strength = "strong"
elif password_length >= 8 and (has_upper or has_lower or has_digit):
    strength = "medium"
else:
    strength = "weak"
 
# Outputs:
if password_valid == True:
    print(strength)

print("----------------------------------")

#Problem 6: Product label formatter (fixed-width text)
print("Problem 6:")

#Description: This exercise focuses on string manipulation and input formatting 
#in Python. The goal is to build a standard product label string with a fixed length
#of 30 characters using string slicing, length checks (len()), 
#conditional statements (if/elif/else), and space padding.

#Validations:
#- product_name must not be empty after strip().
#- price_value must be convertible to a positive number.

#Test cases:
#1) Normal: product_name = "Laptop", price_value = "1200"
#2) Border: product_name = "A"*30, price_value = "0"
#3) Error: product_name = "", price_value = "-5"

# Inputs:
product_name = input("Enter product name: ")
price_value = input("Enter price: ")
 
# Code:
valid_product = True
if (len(product_name.strip()) == 0
        or not price_value.replace(".", "", 1).isdigit()):
    print("Error: Product name cannot be empty and price must be a valid non-negative number.")
    valid_product = False
else:
    base = f"Product: {product_name.strip()} | Price: ${price_value}"

    if len(base) > 30:
        label = base[:30]
    elif len(base) < 30:
        label = base + " " * (30 - len(base))
    else:
        label = base
 
# Outputs:
if valid_product == True:
    print(f'Label: "{label}"')
    print("Length:", len(label))

print("----------------------------------")

#Conclusions:

# 1. El manejo de strings en input y output garantiza una presentación limpia y estructurada.
# 2. Métodos como strip() y lower() limpian espacios y estandarizan entradas.
# 3. Normalizar texto antes de comparar evita errores lógicos por formato.
# 4. Las validaciones evitan fallos de ejecución y el ingreso de datos basura.
# 5. Comprendí que los strings son inmutables y los slices controlan su longitud.

#References:
# 1) Python Software Foundation. Python documentation - Built-in Types:
#    Text Sequence Type — str (documentación oficial traducida al español).
#    https://docs.python.org/es/3/library/stdtypes.html#text-sequence-type-str
#
# 2) Roldán Blay, C. (2021). "Strings en Python" [Video]. Universitat
#    Politècnica de València (UPV).
#    https://riunet.upv.es/handle/10251/167281
#
# 3) Roldán Blay, C. (2021). "Acceso e iteración con strings en Python"
#    [Video]. Universitat Politècnica de València (UPV).
#    https://riunet.upv.es/handle/10251/167347
#
# 4) Platzi. "Métodos de strings en Python: domina el poder de las cadenas
#    de texto" (isalpha, isdigit, strip, replace, etc.).
#    https://platzi.com/blog/metodos-de-strings-en-python-domina-el-poder-de-las-cadenas-de-texto/
#
# 5) LabEx. "Cómo comprobar si una cadena contiene solo letras en Python"
#    (uso de isalpha() para validar la entrada del usuario).
#    https://labex.io/es/tutorials/python-how-to-check-if-a-string-contains-only-letters-in-python-559569