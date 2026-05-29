#personal information
name = 'Jedidah Wangechi'
age = 25
height = 1.65
fav_tech_field = 'Data Science'
student_status = True
fray = '3456'
print(type(fray))
print(f'My name is {name}, I am {age} years old, my height is {height} meters, my favorite technology field is {fav_tech_field}, and it is {student_status} that I am a student.')
#type checker
my_lessons = ['Python', 'Data Analysis', 'Machine Learning']
print(type(name))
print(type(age))
print(type(height))
print(type(fav_tech_field))
print(type(student_status))
print(type(my_lessons))
#data type conversion
print(type(str(age)))
print(type(int(height)))
print(type(str(student_status)))
print(type(int(fray)))
#input function
name = input('What is your name? ')
age = input('What is your age? ')
country = input('Which country do you live in? ')
print('Your name is ' + name + '\n' + 'Your age is ' + age + '\n' + 'You live in ' + country + '.')
#temperature converter
temp_celsius = float(input('Enter temperature in Celsius: '))
temp_fahrenheit = (temp_celsius * 9/5) + 32
print(f'The temperature in Fahrenheit is: {temp_fahrenheit}')