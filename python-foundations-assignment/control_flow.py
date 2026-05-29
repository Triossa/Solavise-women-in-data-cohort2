
#Age eligibility
age = input('Enter your age: ')
if int(age) >= 18:
    print('You are an adult.')
elif int(age) <= 15:
    print('You are a child.')
else:
    print('You are a teenager.')
#password validation
password = input('Enter your password: ')
if len(password) >= 8:
    print('Password is strong.')
else:
    print('Password is weak.')
#grade classification
marks = int(input('Enter your marks: '))
if marks >= 80:
    print('Grade: A' + '\n' + 'EXCELLENT')
elif marks >= 60:
    print('Grade: B' + '\n' + 'GOOD')
elif marks >= 40:
    print('Grade: C' + '\n' + 'AVERAGE')
else:
    print('Grade: D' + '\n' + 'BELOW AVERAGE') 
#multipliation table
number = int(input('Enter a number to display its multiplication table: '))
print(f'Multiplication Table of {number}:')
for i in range(1, 11):
    result = number * i
    print(f'{number} x {i} = {result}')
#guessing game
import random
number_to_guess = random.randint(1, 100)
max_attempts = 6
for attempt in range(1, max_attempts + 1):
    print(f'Attempt {attempt} of {max_attempts}')
    guess = int(input('Guess a number between 1 and 100: '))
    if guess < number_to_guess:
        print('Too low! Guess higher.')
    elif guess > number_to_guess:
        print('Too high! Guess lower.')
    elif guess == number_to_guess:
        print('Congratulations! You guessed the number correctly.')
else:   
    print(f'Sorry, you have used all {max_attempts} attempts. The number was: {number_to_guess}')