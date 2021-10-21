from os import system
from termcolor import colored
from math import pow

def isArmstrong(theData):
    buf=theData
    numberOfDigits=len(str(theData))
    sumation=0
    while(buf>0):
        sumation+=pow(buf%10,numberOfDigits)
        buf=(int)(buf/10)

    if(sumation==theData):
        return True
    else:
        return False        
        

system('clear')
data=int(input('Please enter the desired number : '))

while(data<=0):
    system('clear')
    print(colored('Erorr! your number can not be zro or nrgative. please try again...','red'))
    input()
    system('clear')
    data=int(input('Please enter the desired number : '))

if(isArmstrong(data)==True):
    system('clear')
    print(str(data)+' is Armstrong\n')
else:
    system('clear')
    print(str(data)+' is not Armstrong\n')
