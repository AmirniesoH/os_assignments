from os import system
from time import sleep

system('clear')                                 # Clearing the terminal

weight=float(input('please enter your weight in kilogram : '))

while (weight<=0):                              # Checking the size of weight
    system('clear')                                 # Clearing the terminal

    print('Error! Your weight can not be zero or negative. Please try again...')

    sleep(3.5)                                      # Sleeping the terminal for three seconds
    system('clear')                                 # Clearing the terminal

    weight=float(input('please enter your weight in kilogram : '))

height=float(input('\nplease enter your height in meter : '))

while (height<=0):                              # Check the size of height
    system('clear')                                 # Clearing the terminal

    print('Error! Your height can not be zero or negative. Please try again...')

    sleep(3.5)                                      # Sleeping the terminal for three seconds
    system('clear')                                 # Clearing the terminal

    print('please enter your weight in kilogram : ', weight)

    height=float(input('\nplease enter your height in meter : '))


bodyMassIndex=(weight)/(height**2)              # Calculation body mass index

if (bodyMassIndex<18.5):
    system('clear')                                 # Clearing the terminal

    print('Your body mass index is ', bodyMassIndex,'. This is considered underweight.\n')

elif (bodyMassIndex>=18.5 and bodyMassIndex<25.0):
    system('clear')                                 # Clearing the terminal

    print('Your body mass index is ', bodyMassIndex,'. This is considered normal.\n')

elif (bodyMassIndex>=25.0 and bodyMassIndex<30.0):
    system('clear')                                 # Clearing the terminal

    print('Your body mass index is ', bodyMassIndex,'. This is considered overweight.\n')

elif (bodyMassIndex>=30.0 and bodyMassIndex<35.0):
    system('clear')                                 # Clearing the terminal

    print('Your body mass index is ', bodyMassIndex,'. This is considered obese.\n')

else:                                       # Body mass index >= 35.0
    system('clear')                                 # Clearing the terminal

    print('Your body mass index is ', bodyMassIndex,'. This is considered extremely obese.\n')