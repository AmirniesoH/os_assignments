from os import system
from termcolor import colored
#%%
class Fraction:
    def __init__(self, theNumerator=0, theDenominator=1):
        self.numerator=theNumerator
        self.denominator=theDenominator
   
    def __add__(self, theObject):
        if (self.denominator != theObject.denominator):
            lowestCommonMultiple=self.find_lowestCommonMultiple(self.denominator, (theObject.denominator))
        else:
            lowestCommonMultiple=self.denominator
        return Fraction(self.numerator*int(lowestCommonMultiple/self.denominator) + theObject.numerator*int(lowestCommonMultiple/theObject.denominator), lowestCommonMultiple)   
    
    def __sub__(self, theObject):
        if (self.denominator != theObject.denominator):
            lowestCommonMultiple=self.find_lowestCommonMultiple(self.denominator, (theObject.denominator))
        else:
            lowestCommonMultiple=self.denominator
        return Fraction(self.numerator*int(lowestCommonMultiple/self.denominator) - theObject.numerator*int(lowestCommonMultiple/theObject.denominator), lowestCommonMultiple)   
    
    def __mul__(self, theObject):
        return Fraction(self.numerator*theObject.numerator, self.denominator*theObject.denominator)
    
    def __truediv__(self, theObject):
        return Fraction(self.numerator*theObject.denominator, self.denominator*theObject.numerator)        
    
    def find_lowestCommonMultiple(self, theDataOne, theDataTwo):
        minimum=min(theDataOne,theDataTwo)
        greatestCommonDivisor=0

        for i in range(1, minimum+1):
            if((theDataOne%i==0) and (theDataTwo%i==0)):
                greatestCommonDivisor=i

        return int((theDataOne*theDataTwo)/greatestCommonDivisor)
    def set_numerator(self, theNumerator):
        self.numerator=theNumerator
    def set_denominator(self, theDenominator):
        self.denominator=theDenominator
#%%
def print_MainMenu():
    system('clear')

    print('╒══════════════════════════════════════════════╕')
    print('│              ➊ - Addition                    │')
    print('│              ➋ - Minus                       │')
    print('│              ➌ - Multiplication              │')
    print('│              ➍ - Division                    │')
    print('│              ➎ - Exit                        │')
    print('╘══════════════════════════════════════════════╛\n')

    Choice=int(input('Please Choose your item : '))

    return(Choice)

def print_message(theSentence, theColor):                
    system('clear')
    print(colored(theSentence, theColor))
    input()

#%%
def get_numerator(theKey):
    numerator = int(input('Please enter your desired {} numerator : '.format(theKey)))
    return numerator

def get_denominator(theNumerator, theKey):
    denominator = int(input('\nPlease enter your desired {} denominator : '.format(theKey)))
    while denominator==0:
        print_message('the denominator can not be zero...', 'red')
        system('clear')
        print('Please enter your desired {0} numerator : {1}'.format(theKey, theNumerator))
        denominator = int(input('\nPlease enter your desired {} denominator : '.format(theKey)))
    return denominator

#%%
fractionOne = Fraction()
fractionTwo = Fraction()


numeratorOne=0
numeratorTwo=0
denominatorOne=1
denominatorTwo=1

while True:
    choice=print_MainMenu()
    try:
        match choice:
            case 1: 
                system('clear')
                fractionOne.set_numerator(get_numerator('first'))
                fractionOne.set_denominator(get_denominator(fractionOne.numerator, 'first'))
                system('clear')
                fractionTwo.set_numerator(get_numerator('second'))
                fractionTwo.set_denominator(get_denominator(fractionTwo.numerator, 'second'))
                system('clear')
                result=fractionOne+fractionTwo
                print('{0}/{1} + {2}/{3} = {4}/{5}'.format(fractionOne.numerator, fractionOne.denominator, fractionTwo.numerator, fractionTwo.denominator, result.numerator, result.denominator))
                input()
            case 2:
                system('clear')
                fractionOne.set_numerator(get_numerator('first'))
                fractionOne.set_denominator(get_denominator(fractionOne.numerator, 'first'))
                system('clear')
                fractionTwo.set_numerator(get_numerator('second'))
                fractionTwo.set_denominator(get_denominator(fractionTwo.numerator, 'second'))
                system('clear')
                result=fractionOne-fractionTwo
                print('{0}/{1} - {2}/{3} = {4}/{5}'.format(fractionOne.numerator, fractionOne.denominator, fractionTwo.numerator, fractionTwo.denominator, result.numerator, result.denominator))
                input()
            case 3:
                system('clear')
                fractionOne.set_numerator(get_numerator('first'))
                fractionOne.set_denominator(get_denominator(fractionOne.numerator, 'first'))
                system('clear')
                fractionTwo.set_numerator(get_numerator('second'))
                fractionTwo.set_denominator(get_denominator(fractionTwo.numerator, 'second'))
                system('clear')
                result=fractionOne*fractionTwo
                print('{0}/{1} × {2}/{3} = {4}/{5}'.format(fractionOne.numerator, fractionOne.denominator, fractionTwo.numerator, fractionTwo.denominator, result.numerator, result.denominator))
                input()
            case 4:
                system('clear')
                fractionOne.set_numerator(get_numerator('first'))
                fractionOne.set_denominator(get_denominator(fractionOne.numerator, 'first'))
                system('clear')
                fractionTwo.set_numerator(get_numerator('second'))
                fractionTwo.set_denominator(get_denominator(fractionTwo.numerator, 'second'))
                system('clear')
                result=fractionOne/fractionTwo           
                print('{0}/{1} ÷ {2}/{3} = {4}/{5}'.format(fractionOne.numerator, fractionOne.denominator, fractionTwo.numerator, fractionTwo.denominator, result.numerator, result.denominator))
                input()
            case 5:
                system('clear')
                break
            case _:
                print_message('Erorr! Your choice is incorrect. Please try again...','red')
    except ValueError:
        print_message('your input must be integer...', 'red')    