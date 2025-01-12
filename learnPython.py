#my_name = 'herve' 
#print('my_name:',my_name)

#Asks the user for their age.Prints: "You are [age] years old."

#age = input('enter your age:')
#print(f'you are {age} years old')
"""
x = 3
y = 6
add = x+y
Subtract = x-y
multiply = x*y
divide = x/y
print(f'add ={add},Subtract = {Subtract},multiply ={multiply}, divide = {divide}')

Write a program that:

Asks the user for a number.
Prints whether the number is positive, negative, or zero.

y = float(input('enter a number:'))
if y > 0 :
    print('positive')
elif y < 0 :
    print('negative')
else :
    print('zero')  
    """  
""" 
Exercise 6: Even or Odd
Write a program that:

Asks the user for a number.
Prints whether the number is even or odd.

num = float(input('enter a number:'))
if num % 2 == 0 :
    print('even number')
else:
    print('odd number')
      Write a program that:

Asks the user for their marks (0-100).
Prints the grade based on the following:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: Below 60
    
try:
    # Input score
    score = float(input("Enter the score (0-100): "))
    
    # Determine the grade
    if 90 <= score <= 100:
        grade = "A"
    elif 80 <= score < 90:
        grade = "B"
    elif 70 <= score < 80:
        grade = "C"
    elif 60 <= score < 70:
        grade = "D"
    elif 0 <= score < 60:
        grade = "F"
    else:
        grade = "Invalid score. Please enter a number between 0 and 100."
    
    # Print the grade
    print(f"The grade is: {grade}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
    Write a program to:

Print numbers from 1 to 10 using a for loop.
Print the square of each number.
# Loop through numbers from 1 to 10
for num in range(1, 11):
    # Print the number and its square
    print(f"Number: {num}, Square: {num**2}")

    #########################################
    Write a program that:

Asks the user to guess a secret number (e.g., 7).
Keeps asking until the user guesses correctly.
Prints a congratulatory message when guessed correctly.
    """
    # Secret number to guess
secret_number = 7

# Outer loop for guessing attempts
while True:
    # Inner loop for user input and checking
    guess = input("Guess the secret number (between 1 and 10): ")
    
    # Check if the input is a valid number
    if guess.isdigit():
        guess = int(guess)
        
        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You've guessed the secret number!")
            break  # Exit the loop
        else:
            print("Try again!")
    else:
        print("Please enter a valid number.")