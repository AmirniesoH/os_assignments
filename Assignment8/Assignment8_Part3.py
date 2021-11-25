from os import system
from termcolor import colored


class ComplexNumbers:
    def __init__(self, theComplxNumber=0):
        self.complexNumber=theComplxNumber
    
    def __add__(self, theObject):
        return ComplexNumbers(self.complexNumber + theObject.complexNumber)
    
    def __sub__(self, theObject):
        return ComplexNumbers(self.complexNumber - theObject.complexNumber)
    
    def __mul__(self, theObject):
        return ComplexNumbers(self.complexNumber*theObject.complexNumber)
        
    def print(self):
        print(self.complexNumber, end='')    
    
    def input_console(self, theKey):
        realNumber=float(input('Please enter {} the real number : '.format(theKey)))
        imagNumber=float(input('\nPlease enter {} the imag number : '.format(theKey)))
        self.complexNumber=complex(realNumber, imagNumber)

def print_MainMenu():
    system('clear')

    print('╒══════════════════════════════════════════════╕')
    print('│              ➊ - Addition                    │')
    print('│              ➋ - Minus                       │')
    print('│              ➌ - Multiplication              │')
    print('│              ➍ - Exit                        │')
    print('╘══════════════════════════════════════════════╛\n')

    Choice=int(input('Please Choose your item : '))

    return(Choice)


def print_message(theSentence, theColor):                
    system('clear')
    print(colored(theSentence, theColor))
    input()

complexNumbersOne=ComplexNumbers()
complexNumbersTwo=ComplexNumbers()
result=ComplexNumbers()


while True:
    choice_MainMenu=print_MainMenu()

    match choice_MainMenu:
        case 1:
            system('clear')
            complexNumbersOne.input_console('first')
            system('clear')
            complexNumbersTwo.input_console('second')
            result=complexNumbersOne+complexNumbersTwo
            system('clear')
            complexNumbersOne.print()
            print(' + ', end='')
            complexNumbersTwo.print()
            print(' = ', end='')
            result.print()
            input()
        case 2:
            system('clear')
            complexNumbersOne.input_console('first')
            system('clear')
            complexNumbersTwo.input_console('second')
            system('clear')
            result=complexNumbersOne-complexNumbersTwo
            complexNumbersOne.print()
            print(' - ', end='')
            complexNumbersTwo.print()
            print(' = ', end='')
            result.print()
            input()
        case 3:
            system('clear')
            complexNumbersOne.input_console('first')
            system('clear')
            complexNumbersTwo.input_console('second')
            system('clear')
            result=complexNumbersOne*complexNumbersTwo
            complexNumbersOne.print()
            print(' * ', end='')
            complexNumbersTwo.print()
            print(' = ', end='')
            result.print()
            input()
        case 4:
            system('clear')
            break
        case _:
               print_message('Erorr! Your choice is incorrect. Please try again...','red')


        
        

