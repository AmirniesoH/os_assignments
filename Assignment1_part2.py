from math import pi
from os import system
from time import sleep

radius=float(input('\nPlease enter the size of the radius of your desired circle : '))

while (radius<=0.0):                    # Check the size of the radius
     system('clear')                       # Clear the terminal
     print('Error! the size of the radius can not be negative or zero please try again...')
     sleep(3.5)                            # Pause for three seconds
     system('clear')                       # Clear the terminal
     radius=float(input('Please enter the size of the radius of your desired circle : '))
else:
    area=(radius**2)*pi                    # Calculation area of the circle
    circumference=(radius*2)*pi            # Calculation circumference of the circle

print('\n1) Area of the circle : ', area, '\n\n2) Circumference of the circle : ', circumference, '\n')