#arithmetic operators
num1 = 10
num2 = 5
addition = num1 + num2
subtraction = num1 - num2   
multiplication = num1 * num2
division = num1 / num2
print(f'Addition: {addition}')
print(f'Subtraction: {subtraction}')    
print(f'Multiplication: {multiplication}')
print(f'Division: {division}')
#areas of shapes
radius = 7  
pi = 3.14
area_circle = pi * radius ** 2
print(f'Area of Circle: {area_circle}')
length = 50
width = 30
area_rectangle = length * width
print(f'Area of Rectangle: {area_rectangle}')
base = 20
height = 15
area_triangle = 1/2 * base * height
print(f'Area of Triangle: {area_triangle}')
#even and odd numbers
number = 21
if number % 2 == 0:
    print(f'{number} is an even number.')
else:
    print(f'{number} is an odd number.')
    #percentage score
total_marks = 1000
marks_obtained = 700
percentage_score = marks_obtained / total_marks * 100
print(f'Percentage Score: {percentage_score}%')
#BMI calculator
weight_kg = 70
height_m = 2.76
bmi = weight_kg / height_m ** 2
print(f'BMI: {bmi}')
#power and modulus
base = 5    
exponent = 3
value = base ** exponent
print(f'{base} raised to the power of {exponent} is: {value}')
num1 = 75
num2 = 4
modulus = num1 % num2
print(f'Modulus:{modulus}')
