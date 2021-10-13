from math import pow, sin, cos, tan, log, radians
from os import system
from termcolor import colored

# Other Functions

from os import system

def print_MenuOne():                # Print menu number one
    system('clear')

    print('╒══════════════════════════════════════════════╕')
    print('│               ➊ - Basic Mode                 │')
    print('│               ➋ - Advanced Mode              │')
    print('│               ➌ - Exit                       │')
    print('╘══════════════════════════════════════════════╛\n')

    theChoice=int(input('Please Choose your item : '))

    return(theChoice)

def print_MenuTwo():                # Print menu number two
    system('clear')

    print('╒══════════════════════════════════════════════╕')
    print('│              ➊ - Addition                    │')
    print('│              ➋ - Minus                       │')
    print('│              ➌ - Multiplication              │')
    print('│              ➍ - Division                    │')
    print('│              ➎ - Power                       │')
    print('│              ➏ - Back Page                   │')
    print('╘══════════════════════════════════════════════╛\n')

    theChoice=int(input('Please Choose your item : '))

    return(theChoice)

def print_MenuThree():              # Print menu number three
    system('clear')

    print('╒══════════════════════════════════════════════╕')
    print('│                ➊ - Logarithm                 │')
    print('│                ➋ - Sine                      │')
    print('│                ➌ - Cosine                    │')
    print('│                ➍ - Tangent                   │')
    print('│                ➎ - Cotangent                 │')
    print('│                ➏ - Back Page                 │')
    print('╘══════════════════════════════════════════════╛\n')

    theChoice=int(input('Please Choose your item : '))

    return(theChoice)

def add(theDataOne, theDataTwo):
    return(theDataOne+theDataTwo)

def subtract(theDataOne, theDataTwo):
    return(theDataOne-theDataTwo)

def multiply(theDataOne, theDataTwo):
    return (theDataOne*theDataTwo)

def divide(theDataOne, theDataTwo):
    return(theDataOne/theDataTwo)  


# Main Function-----------------------------


flagMenuOne=True

while(flagMenuOne):
    choiceMenuOne=print_MenuOne()

    if (choiceMenuOne==1):
        flagMenuTwo=True

        while(flagMenuTwo):
            choiceMenuTwo=print_MenuTwo()

            if(choiceMenuTwo==1):
                system('clear')
                dataOne = float(input('\nPlease enter your first desired number : '))
                dataTwo = float(input('\nPlease enter your second desired number : '))
                print('\nResult: '+ str(dataOne) + ' + ' + str(dataTwo) + ' = ' + str(add(dataOne, dataTwo)) +'\n')
                input()
            elif(choiceMenuTwo==2):
                system('clear')
                dataOne = float(input('\nPlease enter your first desired number : '))
                dataTwo = float(input('\nPlease enter your second desired number : '))
                print('\nResult: '+ str(dataOne) + ' - ' + str(dataTwo) + ' = ' + str(subtract(dataOne, dataTwo)) +'\n')
                input()
            elif(choiceMenuTwo==3):
                system('clear')
                dataOne = float(input('\nPlease enter your first desired number : '))
                dataTwo = float(input('\nPlease enter your second desired number : '))
                print('\nResult: '+ str(dataOne) + ' × ' + str(dataTwo) + ' = ' + str(multiply(dataOne, dataTwo)) +'\n') 
                input()  
            elif(choiceMenuTwo==4):
                system('clear')
                dataOne = float(input('\nPlease enter your first desired number : '))
                dataTwo = float(input('\nPlease enter your second desired number : '))
                if(dataTwo==0):
                    system('clear')
                    print(colored('Erorr! The second number can not be zero...','red'))
                    input()
                else:    
                    print('\nResult: '+ str(dataOne) + ' ÷ ' + str(dataTwo) + ' = ' + str(divide(dataOne, dataTwo)) +'\n')
                    input()
            elif(choiceMenuTwo==5):
                system('clear')
                dataOne = float(input('\nPlease enter your desired base number : '))
                dataTwo = float(input('\nPlease enter your desired exponent number : '))
                print('\nResult: '+ str(dataOne) + ' ^ ' + str(dataTwo) + ' = ' + str(pow(dataOne, dataTwo)) +'\n')
                input()
            elif(choiceMenuTwo==6):
                flagMenuTwo=False
            else:
                system('clear')    
                print('Your choice is false please try again...')
                input()
    elif(choiceMenuOne==2):
        flagMenuThree=True

        while(flagMenuThree):
            choiceMenuThree=print_MenuThree()

            if(choiceMenuThree==1):
                system('clear')
                dataOne = float(input('\nPlease enter your desired argument : '))
                while(dataOne<=0):
                    system('clear')
                    print(colored('Erorr! the argumant can not be zero or negative...','red'))
                    input()
                    system('clear')
                    dataOne = float(input('\nPlease enter your desired argument : '))

                dataTwo = float(input('\nPlease enter your desired base number : '))
                while(dataTwo<=0 or dataTwo==1):
                    system('clear')
                    print(colored('Erorr! the base number can not be zero or one or negative...','red'))
                    input()
                    system('clear')
                    print('Please enter your desired argument : '+str(dataOne))
                    dataTwo = float(input('\nPlease enter your desired base number : '))
                else:
                    print('\nResult: '+ str(log(dataOne, dataTwo)) + ' is the loarithm of '+ str(dataOne)+' to the base '+str(dataTwo))
                    input()
            elif(choiceMenuThree==2):
                system('clear')
                dataOne=float(input('Please enter the size of your desired angle in degrees : '))
                print('\nResult: sin('+str(dataOne)+') = '+str(sin(radians(dataOne))))   
                input()
            elif(choiceMenuThree==3):
                system('clear')
                dataOne=float(input('Please enter the size of your desired angle in degrees : '))
                print('\nResult: cos('+str(dataOne)+') = '+str(cos(radians(dataOne))))   
                input()   
            elif(choiceMenuThree==4):
                system('clear')
                dataOne=float(input('Please enter the size of your desired angle in degrees : '))
                print('\nResult: tan('+str(dataOne)+') = '+str(tan(radians(dataOne))))   
                input()
            elif(choiceMenuThree==5):
                system('clear')
                dataOne=float(input('Please enter the size of your desired angle in degrees : '))
                print('\nResult: cot('+str(dataOne)+') = '+str(1/tan(radians(dataOne))))   
                input()
            elif(choiceMenuThree==6):
                flagMenuThree=False
            else:
                system('clear')    
                print('Your choice is false please try again...')
                input()
    elif(choiceMenuOne==3):
        flagMenuOne=False
    else:
        system('clear')    
        print('Your choice is false please try again...')
        input()                