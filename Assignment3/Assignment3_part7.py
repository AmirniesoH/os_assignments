from os import system
from termcolor import colored


def find_greatestCommonDivisor(theDataOne, theDataTwo):
    minimum=min(theDataOne,theDataTwo)
    greatestCommonDivisor=0

    for i in range(1, minimum+1):
        if((theDataOne%i==0) and (theDataTwo%i==0)):
            greatestCommonDivisor=i

    return greatestCommonDivisor        

system('clear')
dataOne=int(input('please enter the desired first number : '))     

while(dataOne<=0):
    system('clear')
    print(colored('Erorr! your number can not be zro or nrgative. please try again...','red'))
    input()
    system('clear')
    dataOne=int(input('please enter the desired first number : '))    

dataTwo=int(input('\nplease enter the desired second number : ')) 

while(dataTwo<=0):
    system('clear')
    print(colored('Erorr! your number can not be zro or nrgative. please try again...','red'))
    input()
    system('clear')
    print('please enter the desired first number : '+str(dataOne))
    dataTwo=int(input('\nplease enter the desired second number : '))

system('clear')
print('The greatest divisor of the common '+str(dataOne)+' and '+str(dataTwo)+' is equal to '+str(find_greatestCommonDivisor(dataOne, dataTwo))+'\n')        
