#Manejo de números y booleanos en Python
#Nombre:César Enrique García Samano
#Matricula: 2630328
#Grupo: M1-1

print("----------------------------------")

# Resumen ejecutivo

# 1. ¿Qué son los tipos int y float en Python?
# El tipo int permite almacenar números enteros, como 5, 10 o -3.
# El tipo float permite almacenar números decimales, como 3.5 o 2.75.
# La diferencia es que int no utiliza decimales, mientras que float sí.

# 2. ¿Qué es un booleano y cómo se obtiene?
# Un booleano (bool) es un tipo de dato que puede tener dos valores: True o False.
# Se obtiene mediante comparaciones, como 5 > 3, que devuelve True.

# 3. ¿Por qué es importante validar los datos?
# Validar rangos ayuda a evitar valores incorrectos y errores en los cálculos.
# También es importante evitar la división entre cero, ya que provoca un error.

# 4. ¿Qué cubrirá el documento?
# Se describirán los problemas, sus entradas y salidas, las validaciones aplicadas
# y el uso de int, float y booleanos para realizar cálculos y tomar decisiones.

print("----------------------------------")

#Problem 1: Temperature converter and range flag
print("Problem 1:")

#Description: Convert a temperature in degrees Celsius (float) to Fahrenheit and Kelvin.
#Additionally, determine a Boolean value called is_high_temperature that is True if 
#the temperature in Celsius is greater than or equal to 30.0, and False otherwise.

#Validations:
#Verify that temp_c can be converted to a float.
#Do not allow physically impossible temperatures in Kelvin (for example, temp_k < 0.0).

#Test cases:
# Normal: input 25
#   -> Fahrenheit:77.0, Kelvin:298.15, High_Temperature:False
# Edge:   input 30
#   -> Fahrenheit:86.0, Kelvin:303.15, High_Temperature:True
# Error:  input -300
#   -> Kelvin: "Error: Physically impossible temperature (below absolute zero)."

#inputs:
temp_c = float(input("enter temperature in °C:"))

#code:

if temp_c >= 30:
    is_high_temperature = True
else:
    is_high_temperature = False 

temp_f = temp_c * 9/5 + 32
temp_k = temp_c + 273.15

if temp_k < 0.0:
    temp_k = "Error: Physically impossible temperature (below absolute zero)."

#output:
print(f"Fahrenheit:{temp_f}")
print(f"Kelvin:{temp_k}")
print(f"High_Temperature:{is_high_temperature}")

print("----------------------------------")

#Problem 2: Work hours and overtime payment
print("Problem 2:")

#Description:
#Calculate the total weekly pay of a worker.
#Up to 40 hours are paid at the hourly_rate (float). 
#Overtime hours (> 40) are paid at 150% of the normal rate.
#Additionally, generate a Boolean value called has_overtime that indicates whether
#the worker worked overtime.

#Validations:
# hours_worked >= 0
# hourly_rate > 0
# If either condition is not met, display "Error: invalid input".

#Test cases:
# Normal: hours_worked = 45, hourly_rate = 100
#   -> regular pay: 4000.0, overtime pay: 750.0, Total_pay: 4750.0, Has overtime: True
# Edge:   hours_worked = 40, hourly_rate = 100
#   -> regular pay: 4000.0, overtime pay: 0.0, Total_pay: 4000.0, Has overtime: False
# Error:  hours_worked = -5, hourly_rate = 100
#   -> Error: invalid input

#inputs:
hours_worked = float(input("hours worked: "))
hourly_rate = float(input("hourly rate: "))

# code:
valid_hours = True
regular_pay = 0.0
overtime_pay = 0.0
has_overtime = False

if hours_worked < 0 or hourly_rate <= 0:
    valid_hours = False
    print("Error: invalid input")
else:
    if hours_worked > 40:
        has_overtime = True
        regular_pay = 40 * hourly_rate
        overtime_pay = (hours_worked - 40) * hourly_rate * 1.5
    else:
        regular_pay = hours_worked * hourly_rate

    total_pay = regular_pay + overtime_pay

# output:
if valid_hours:
    print(f"regular pay: {regular_pay}")
    print(f"overtime pay: {overtime_pay}")
    print(f"Total_pay: {total_pay}")
    print(f"Has overtime: {has_overtime}")

print("----------------------------------")

#Problem 3: Discount eligibility with booleans
print("Problem 3:")

#Determine whether a customer qualifies for a discount on their purchase. The rule is:
#- The customer gets a discount if:
#- is_student is True, OR
#- is_senior is True, OR
#- purchase_total >= 1000.0

#Validations:
# purchase_total >= 0.0
# Normalize is_student_text and is_senior_text to uppercase and convert them into the Boolean values is_student and is_senior.
# If the text is neither "YES" nor "NO", display "Error: invalid input".

#Test cases:
# Normal: purchase_total = 500, is_student = NO, is_senior = NO
#   -> Discount eligible:False, Final total: 500.0
# Edge:   purchase_total = 1000, is_student = NO, is_senior = NO
#   -> Discount eligible:True, Final total: 900.0
# Error:  purchase_total = 500, is_student = MAYBE, is_senior = NO
#   -> Error: invalid input

#inputs:
purchase_total = float(input("purchase total:"))
is_student_text = input("is student:").upper()
is_senior_text = input("is senior:").upper()

#code:
is_student = False
is_senior = False
customer = True 
discount_eligible = False

if is_student_text not in ["YES", "NO"] or is_senior_text not in ["YES", "NO"] or purchase_total < 0:
    print("Error: invalid input")
    customer = False
else:
    is_student = (is_student_text == "YES")
    is_senior = (is_senior_text == "YES")

    if is_student or is_senior or purchase_total >= 1000.0:
        discount_eligible = True
        purchase_total = purchase_total * 0.90

#output:
if customer:
    print(f"Discount eligible:{discount_eligible}")
    print(f"Final total: {purchase_total}") 

print("----------------------------------")

#Problem 4: Basic statistics of three integers
print("Problem 4:")

#Description:
#Read three integers and calculate the sum, average (float), maximum value, minimum value, 
#and a Boolean value called all_even that indicates whether all three numbers are even.

#Validations:
# Verify that all three values can be converted to int.
# No additional restrictions are required (negative numbers are allowed).

#Test cases:
# Normal: inputs 2, 4, 6
#   -> Sum:12, Average:4.0, max:6, min:2, All even:True
# Edge:   inputs 0, -2, -4 (zero and negative numbers)
#   -> Sum:-6, Average:-2.0, max:0, min:-4, All even:True
# Error:  inputs abc, 4, 6
#   -> Error: invalid input (the input is not an integer)

#inputs:
n1 = int(input("insert number one:"))
n2 = int(input("insert number two:"))
n3 = int(input("insert number three:"))

#code:
all_even = False
sum_value = n1 + n2 + n3
average_value = sum_value / 3
if (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0):
    all_even = True

#output:
print(f"Sum:{sum_value}")
print(f"Average:{average_value}")
print(f"max:{max(n1, n2, n3)}")
print(f"min:{min(n1, n2, n3)}")
print(f"All even:{all_even}")

print("----------------------------------")

#Problem 5: Loan eligibility (income and debt ratio)
print("Problem 5:")

# Description:
# Determine whether a person is eligible for a loan based on:
# - monthly_income (float)
# - monthly_debt (float)
# - credit_score (int)
# The rule is:
# - debt_ratio = monthly_debt / monthly_income
# - eligible is True if:
#   - monthly_income >= 8000.0 AND
#   - debt_ratio <= 0.4 AND
#   - credit_score >= 650

# Validations:
# - monthly_income > 0.0 (to avoid division by zero).
# - monthly_debt >= 0.0
# - credit_score >= 0
# - If any condition is not met, display "Error: invalid input".

#Test cases:
# Normal: monthly_income = 10000, monthly_debt = 2000, credit_score = 700
#   -> Debt ratio:0.2, Eligible:True
# Edge:   monthly_income = 8000, monthly_debt = 3200, credit_score = 650
#   -> Debt ratio:0.4, Eligible:True
# Error:  monthly_income = 0, monthly_debt = 500, credit_score = 700
#   -> Error: invalid input

#inputs:
monthly_income = float(input("Monthly income:"))
monthly_debt = float(input("monthly debt:"))
credit_score = int(input("Credit score:"))

#code:
valid_pass = True 
eligible = False

if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
    print("Error: invalid input")
    valid_pass = False
else:
    debt_ratio = monthly_debt / monthly_income
    if monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650:
        eligible = True
    
#output:
if valid_pass:
    print(f"Debt ratio:{debt_ratio}")
    print(f"Eligible:{eligible}")

print("----------------------------------")

#Problem 6: Body Mass Index (BMI) and category flag
print("Problem 6:")

# Description:
# Calculate a person's Body Mass Index (BMI) using the formula:
# - bmi = weight_kg / (height_m * height_m)
# Additionally, generate Boolean values to indicate:
# - is_underweight (bmi < 18.5)
# - is_normal (18.5 <= bmi < 25.0)
# - is_overweight (bmi >= 25.0)

# Validations:
# - weight_kg > 0.0
# - height_m > 0.0
# - If either condition is not met, display "Error: invalid input".

#Test cases:
# Normal: weight_kg = 70, height_m = 1.75
#   -> BMI:22.86, Underweight:False, Normal:True, Overweight:False
# Edge:   weight_kg = 100, height_m = 2.0
#   -> BMI:25.0, Underweight:False, Normal:False, Overweight:True
# Error:  weight_kg = 0, height_m = 1.75
#   -> Error: invalid input

#inputs:
weight_kg  = float(input("weight in kilogram:"))
height_m = float(input("height in meters:"))

#code:
bmi_valid = True
is_underweight = False
is_normal = False
is_overweight = False

if weight_kg <= 0.0 or height_m <= 0.0:
    print("Error: invalid input")
    bmi_valid = False
else:
    bmi = weight_kg / (height_m * height_m)
    if bmi < 18.5:
        is_underweight = True
    elif 18.5 <= bmi < 25.0:
        is_normal = True
    else:
        is_overweight = True

#output:
if bmi_valid:
    print(f"BMI:{round(bmi, 2)}")
    print(f"Underweight:{is_underweight}")
    print(f"Normal:{is_normal}")
    print(f"Overweight:{is_overweight}")

print("----------------------------------")

# Conclusions:
# 1. Enteros y flotantes se combinan fluidamente para modelar datos numéricos del mundo real con precisión.
# 2. Las comparaciones generan valores booleanos clave para activar estructuras condicionales (if) y guiar el flujo.
# 3. Validar rangos y prevenir divisiones entre cero garantiza la robustez y evita caídas imprevistas del sistema.
# 4. El uso de condiciones combinadas (and, or, not) permite estructurar la lógica para escenarios complejos.
# 5. Estos patrones repetitivos son la base de aplicaciones prácticas como nóminas, descuentos y préstamos.

# References:
# 1) Python Software Foundation. Python documentation - Built-in Types:
#    Numeric Types — int, float, complex (documentación oficial traducida al español).
#    https://docs.python.org/es/3/library/stdtypes.html
#
# 2) Python Software Foundation. Python documentation - Boolean Type — bool
#    y operaciones booleanas (and, or, not).
#    https://docs.python.org/es/3/library/stdtypes.html
#
# 3) Díaz, J. (Píldoras Informáticas). "Curso Python. Condicionales I. Vídeo 10" [Video].
#    https://www.youtube.com/watch?v=cf7o4s9nFu8
#
# 4) Código Facilito. "Curso de fundamentos de Python - COMPLETO" [Video].
#    https://www.youtube.com/watch?v=Nvm7JzhUpc4
#
# 5) Python Software Foundation. Python documentation - Errores y excepciones:
#    Manejo de ZeroDivisionError y validación de entradas de usuario.
#    https://docs.python.org/es/3/tutorial/errors.html