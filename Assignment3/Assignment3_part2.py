from os import system
from random import randint
from termcolor import colored

system('clear')

myList=[]
sizeList=int(input('Please enter the desired list size : '))


while sizeList>99 or sizeList<0:
    system('clear')
    print(colored('Erorr! the size of lise can not be zero or negative or bigger than Hundred... ','red'))
    input()
    system('clear')
    sizeList=int(input('Please enter the desired list size : '))

i=0
while(i<sizeList):
    randomNumber=randint(0,100)

    if randomNumber not in myList:
        myList.append(randomNumber)
        i+=1

system('clear')
print('theList=[', end='')

for i in range(sizeList):
    print(str(myList[i]),end='')
    
    if i!=sizeList-1:
        print(',',end=' ')
    else:
        print(']\n')    
