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
    """ 
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

