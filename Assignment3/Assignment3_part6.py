from os import system
from termcolor import colored


def isSorted(theData):
    for i in range(len(theData)-1):
        if(theData[i]<theData[i+1]):
            return True
        else:
            return False    




system('clear')

data=[]
sizeData=int(input('Please enter the desired list size : '))

while(sizeData<=0):
    system('clear')
    print(colored('Erorr! your number can not be zro or nrgative. please try again...','red'))
    input()
    system('clear')
    sizeData=int(input('Please enter the desired list size : '))

system('clear')

for i in range(sizeData):
    data.append(input('Please enter the desired list (Number '+str(i+1)+') : ' ))
    print('\n')


if isSorted(data)==True:
    system('clear')
    print( 'your list is Sorted\n')
else:
    system('clear')
    print( 'your list is not Sorted\n')