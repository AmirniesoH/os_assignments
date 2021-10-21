from math import factorial
from os import system
from termcolor import colored

def isFactorizable(theData):
    counter=1
    while(True):
        if(factorial(counter)==theData):
            return True
        elif factorial(counter)>theData:
            return False
        else:
            counter+=1

system('clear')
data=int(input('Please enter the desired number : '))

while(data<=0):
    system('clear')
    print(colored('Erorr! your number can not be zro or nrgative. please try again...','red'))
    input()
    system('clear')
    data=int(input('Please enter the desired number : '))

if(isFactorizable(data)==True):
    system('clear')
    print(str(data)+' is factorizable')
else:
    system('clear')
    print(str(data)+' is not factorizable\n')    

