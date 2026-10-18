#Manejo de Listas, Tuplas y Diccionarios en Python
#Nombre:César Enrique García Samano
#Matricula: 2630328
#Grupo: M1-1

print("----------------------------------")

# Resumen ejecutivo

# 1. Listas, tuplas y diccionarios: Las listas son colecciones ordenadas mutables,
#las tuplas son inmutables y los diccionarios manejan pares clave-valor.
# 2. Mutabilidad: Una lista puede ser modificada después de crearse, mientras
#que una tupla es fija e inalterable (inmutable).
# 3. Diccionarios: Permiten asociar claves únicas con valores para realizar
#búsquedas rápidas y asociativas de datos.
# 4. Cobertura del documento: Se describirá la resolución de problemas, diseño 
#de E/S, validaciones y aplicaciones prácticas en catálogos y registros.

print("----------------------------------")

#Problem 1: Shopping list basics (list operations)
print("Problem 1:")

# Description:
# Work with a list of products (strings) and their quantities (integers). The program must:
# 1) Create an initial list of products.
# 2) Allow adding a new product at the end.
# 3) Display the total number of elements in the list.
# 4) Check whether a specific product is in the list (Boolean value is_in_list).

# Validations:
# - initial_items_text must not be empty after strip().
# - Split the string by commas and remove extra spaces from each element.
# - new_item and search_item must not be empty.
# - Handle the case of an empty initial list if the student chooses to do so (document the decision).

# Test cases:
# 1) Normal: initial="apple,banana,orange", new="grape", search="banana"
# 2) Border: initial="  milk  ", new="bread", search="milk"
# 3) Error: initial="" or "   ", new="apple", search="banana" (empty initial items)

#Inputs:
initial_items_text = input("Enter initial items (comma-separated): ")
new_item = input("Enter a new item to add: ")
search_item = input("Enter an item to search: ")

#Code:
valid_process = True
items_list = []
total_items = 0
is_in_list = False

initial_clean = initial_items_text.strip().lower()
new_clean = new_item.strip().lower()
search_clean = search_item.strip().lower()

if initial_clean == "":
    print("Error: Initial items text cannot be empty or contain only spaces.")
    valid_process = False
elif new_clean == "":
    print("Error: The new item cannot be empty.")
    valid_process = False
elif search_clean == "":
    print("Error: The search item cannot be empty.")
    valid_process = False
else:
    #Create initial list: split by commas and strip extra spaces for each element
    items_list = [item.strip() for item in initial_clean.split(",") if item.strip()]

    if len(items_list) == 0:
        print("Error: Initial items must contain at least one valid product.")
        valid_process = False
    else:
        #Add the new product to the end of the list using append()
        items_list.append(new_clean)
    
        #Get the total quantity of items using len()
        total_items = len(items_list)
    
        #Verify if the search item is in the list using the 'in' operator
        is_in_list = search_clean in items_list

#Outputs:
if valid_process:
    print(f"Items list: {items_list}")
    print(f"Total items: {total_items}")
    print(f"Found item: {str(is_in_list)}")

print("----------------------------------")

#Problem 2: Points and distances with tuples
print("Problem 2:")

# Description: Program to represent 2D points using tuples, calculate the 
# Euclidean distance between them, and find their midpoint with input validation.

# Validations:
# - Verify that all four inputs can be converted to float.
# - No additional range restrictions are required.

# Test cases:
# 1) Normal: x1=0.0, y1=0.0, x2=3.0, y2=4.0
# 2) Border: x1=-1.5, y1=2.5, x2=-1.5, y2=2.5
# 3) Error: x1="abc", y1=1.0, x2=2.0, y2=3.0 (non-numeric input)

#Inputs:
raw_x1 = input("Enter x1: ")
raw_y1 = input("Enter y1: ")
raw_x2 = input("Enter x2: ")
raw_y2 = input("Enter y2: ")

#Code:
valid_inputs = True
x1, y1, x2, y2 = 0.0, 0.0, 0.0, 0.0
distance = 0.0
midpoint = (0.0, 0.0)

try:
    x1 = float(raw_x1.strip())
    y1 = float(raw_y1.strip())
    x2 = float(raw_x2.strip())
    y2 = float(raw_y2.strip())
except ValueError:
    print("Error: All coordinates must be valid numeric values (floats or integers).")
    valid_inputs = False

if valid_inputs:
    #Create tuples for point A and point B
    point_a = (x1, y1)
    point_b = (x2, y2)
    
    #Calculate Euclidean distance
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    #Create a new tuple for the midpoint
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

#Outputs:
if valid_inputs:
    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {distance}")
    print(f"Midpoint: {midpoint}")

print("----------------------------------")

#Problem 3: Product catalog with dictionary
print("Problem 3:")

# Description:
# Manage a small product catalog using a dictionary where:
# - Key: product name (string).
# - Value: unit price (float).
# The program must:
# 1) Create an initial dictionary with at least 3 products.
# 2) Read a product name and the quantity to purchase.
# 3) Calculate the total amount to pay if the product exists.
# 4) If the product does not exist, display an error message.

# Validations:
# - quantity > 0.
# - product_name must not be empty after strip().
# - Check whether product_name exists in the dictionary (key).

# Test cases:
# 1) Normal: product_name="apple", quantity=3
# 2) Border: product_name="banana", quantity=1
# 3) Error: product_name="orange", quantity=2 (product not found)

#Inputs:
product_name = input("Enter product name: ")
quantity = input("Enter quantity: ")

#Code:
valid_purchase = True
unit_price = 0.0
total_price = 0.0
parsed_quantity = 0

#Initial dictionary of products
product_prices = {
    "apple": 10.0,
    "banana": 5.5,
    "milk": 18.25
}

product_clean = product_name.strip().lower()
quantity_clean = quantity.strip()

if product_clean == "":
    print("Error: Product name cannot be empty.")
    valid_purchase = False
elif not quantity_clean.isdigit():
    print("Error: Quantity must be a valid integer.")
    valid_purchase = False
else:
    parsed_quantity = int(quantity_clean)
    
    if parsed_quantity <= 0:
        print("Error: Quantity must be greater than 0.")
        valid_purchase = False
    elif product_clean not in product_prices:
        print("Error: Product not found")
        valid_purchase = False
    else:
        unit_price = product_prices[product_clean]
        total_price = unit_price * parsed_quantity
        quantity = parsed_quantity

#Outputs:
if valid_purchase:
    print(f"Unit price: {unit_price}")
    print(f"Quantity: {quantity}")
    print(f"Total: {total_price}")

print("----------------------------------")

#Problem 4: Student grades with dict and list
print("Problem 4:")

# Description:
# Manage a group's grades using a dictionary:
# - Key: student name (string).
# - Value: list of grades (list of float).
# The program must:
# 1) Create a dictionary with at least 3 students, each with a list of grades.
# 2) Read a student's name.
# 3) Calculate the average of their grades.
# 4) Indicate whether the student passed (average >= 70.0) using a Boolean value called is_passed.

# Validations:
# - student_name must not be empty after strip().
# - Check whether student_name is a key in the dictionary.
# - Verify that the list of grades is not empty before calculating the average.

# Test cases:
# 1) Normal: student_name="Wilbur"
# 2) Border: student_name="  astra  " (tests stripping spaces and automatic capitalization)
# 3) Error: student_name="John" (student not found) or student_name="" (empty name)

#Inputs:

student_name = input("Enter a student first name:")

#Code:
student_in_list = True
is_passed = False

students_grade = {
    "Wilbur":[90, 89, 100],
    "Astra":[81,92,88],
    "Gerard":[76,55,75]
}

student_name_clean = student_name.strip().capitalize()

if student_name_clean == "":
    print("Error: Student name cannot be empty.")
    student_in_list = False
elif student_name_clean not in students_grade:
    print("Error: Student not found")
    student_in_list = False
else:
    grades = students_grade[student_name_clean]

    if len(grades) == 0:
        print("Error: The list of grades cannot be empty")
        student_in_list = False
    else:
        average = sum(grades) / len(grades)
        if average >= 70.0:
            is_passed = True

#Output:
if student_in_list:
    print(f"Grades:{grades}")
    print(f"Average:{average}")
    print(f"Passed:{is_passed}")

print("----------------------------------")

#Problem 5: Word frequency counter (list + dict)
print("Problem 5:")

# Description:
# Count the frequency of each word in a sentence using:
# - A list of words.
# - A dictionary where:
#   - Key: word (string).
#   - Value: frequency (int).
# The program must:
# 1) Read a sentence.
# 2) Convert it to lowercase and split it into a list of words.
# 3) Build a frequency dictionary.
# 4) Display the complete dictionary and the most frequent word.

# Validations:
# - sentence must not be empty after strip().
# - Handle simple punctuation marks if the student chooses to do so (document the decision, for example, by using replace()).
# - Verify that the list of words is not empty.

# Test cases:
# 1) Normal: sentence="Hello world hello python"
# 2) Border: sentence="  Python, python, python!  " (spaces, mixed capitalization, and punctuation)
# 3) Error: sentence="" or sentence="   " (empty sentence)

#Inputs:
sentence = input("Enter a sentence: ")

#Code:
valid_sentence = True
words_list = []
freq_dict = {}
most_common_word = ""

sentence_clean = sentence.strip()

if sentence_clean == "":
    print("Error: Sentence cannot be empty or contain only spaces.")
    valid_sentence = False
else:
    punctuation_marks = [",", ".", "!", "?", ";", ":", "¿", "¡", '"', "(", ")"]
    for mark in punctuation_marks:
        sentence_clean = sentence_clean.replace(mark, " ")

    words_list = sentence_clean.lower().split()

    if len(words_list) == 0:
        print("Error: Words list cannot be empty.")
        valid_sentence = False
    else:
        #Build frequency dictionary using conditional check (without try-except)
        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        #Find the most frequent word
        max_freq = -1
        for word in freq_dict:
            if freq_dict[word] > max_freq:
                max_freq = freq_dict[word]
                most_common_word = word

#Outputs:
if valid_sentence:
    print(f"Words list: {words_list}")
    print(f"Frequencies: {freq_dict}")
    print(f"Most common word: {most_common_word}")

print("----------------------------------")

#Problem 6: Simple contact book (dictionary CRUD)
print("Problem 6:")

# Description:
# Implement a mini "contact book" using a dictionary where:
# - Key: contact name (string).
# - Value: phone number (string).
# The program must:
# 1) Create an initial dictionary with some contacts.
# 2) Read an action called action_text ("ADD", "SEARCH", or "DELETE").
# 3) Depending on the action:
#    - "ADD": read name and phone, then add or update the contact.
#    - "SEARCH": read name and display the phone number if it exists.
#    - "DELETE": read name and delete the contact if it exists.
# 4) Display a message indicating the result of the operation.

# Validations:
# - Normalize action_text to uppercase.
# - Verify that action_text is one of the three valid options.
# - name must not be empty after strip().
# - For "ADD": phone must not be empty after strip().

# Test cases:
# 1) Normal (Add): action_text="ADD", name_contact="  sasha  ", phone="8341112233" (tests stripping, title case, and adding to dictionary)
# 2) Normal (Search): action_text="SEARCH", name_contact="Eren" (tests searching for an existing contact and retrieving its phone)
# 3) Normal (Deleted): action_text="DELETE", name_contact="Armin" (tests popping/deleting an existing contact successfully)
# 4) Border/Update (Add): action_text="ADD", name_contact="bill", phone="555999" (tests updating an existing key with new values)
# 5) Error (Action): action_text="UPDATE", name_contact="Mikasa", phone="1234" (tests invalid menu action handling)
# 6) Error (Empty name): action_text="SEARCH", name_contact="   " (tests empty string validation with spaces)
# 7) Error (Not found): action_text="DELETE", name_contact="Connie" (tests handling when a contact does not exist)

#Inputs:
action_text = input("Enter ADD, SEARCH or DELETE a contact:")

#Code:
valid_action = True 
action_add = False
action_search = False
action_delete = False

contacts = {
    "Bill": "83418734498",
    "Armin": "8346767676",
    "Eren": "8346666666"
}

action_capital = action_text.upper().strip()

if action_capital == "":
    print("Error: Action cannot be empty or contain only spaces.")
    valid_action = False
elif action_capital not in ("ADD", "SEARCH", "DELETE"):
    print("Error: No Valid Action")
    valid_action = False
else:
    if action_capital == "ADD":
        name_contact = input("name contact:")
        phone = input("phone:")
        name_clean = name_contact.strip().title()
        phone_clean = phone.strip()
        if name_clean == "":
            print("Error: Name cannot be empty or contain only spaces")
            valid_action = False
        elif phone_clean == "":
            print("Error: Phone cannot be empty")
            valid_action = False
        else: 
            contacts[name_clean] = phone_clean
            action_add = True

    elif action_capital == "SEARCH":
        name_contact = input("name contact:")
        name_clean = name_contact.strip().title()
        if name_clean == "":
            print("Error: Name cannot be empty or contain only spaces")
            valid_action = False
        elif name_clean not in contacts:
            print("Error: Contact not found")
            valid_action = False
        else:
            phone_found = contacts[name_clean]
            action_search = True
    else:
        name_contact = input("name contact:")
        name_clean = name_contact.strip().title()
        if name_clean == "":
            print("Error: Name cannot be empty or contain only spaces")
            valid_action = False
        elif name_clean not in contacts:
              print("Error: Contact not found")
              valid_action = False
        else:
            phone_deleted = contacts.pop(name_clean)
            action_delete = True

#Output:
if action_add:
    print(f"Success! Contact '{name_clean}' with phone '{phone_clean}' saved/updated.")
    print("Updated dictionary:", contacts)         
elif action_search:
    print(f"Contact found! Name: {name_clean}, Phone: {phone_found}")
elif action_delete:
    print(f"Success: Contact '{name_clean}' has been deleted.")
    print("Updated dictionary:", contacts) 

print("----------------------------------")

#Conclusions:
# Las listas convienen para colecciones ordenadas y flexibles, las tuplas para datos fijos y los diccionarios para buscar por clave.
# Las listas permiten agregar y eliminar elementos de forma dinámica, adaptándose perfectamente a los cambios durante la ejecución.
# Las tuplas son sumamente útiles para proteger información que no debe cambiar jamás, garantizando seguridad mediante inmutabilidad.
# Los diccionarios facilitan búsquedas rápidas al mapear claves únicas directamente con sus valores asociados.
# Combinar estructuras complejas, como un diccionario de listas, permite modelar y organizar múltiples datos de forma avanzada.

# References:
# 1) Python Software Foundation. Python documentation - Estructuras de datos:
#    Listas, tuplas y diccionarios (documentación oficial).
#    https://docs.python.org/es/3/tutorial/datastructures.html
#
# 2) Real Python. "Python Data Structures: Lists, Tuples, Dictionaries, and Sets"
#    https://realpython.com/learning-paths/basic-python-data-structures/
#
# 3) Al Sweigart. "Automate the Boring Stuff with Python: Practical Programming for Total Beginners"
#    Chapter 4: Lists y Chapter 5: Dictionaries and Structuring Data.
#    https://automatetheboringstuff.com/
#
# 4) Código Facilito. "Curso profesional de Python - Listas, Tuplas y Diccionarios" [Video].
#    https://www.youtube.com/watch?v=Nvm7JzhUpc4
#
# 5) Python Software Foundation. Python documentation - Built-in Types:
#    dict, list, tuple y métodos de mapeo/secuencias.
#    https://docs.python.org/es/3/library/stdtypes.html


    



