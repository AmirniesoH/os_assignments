from os import system
from time import sleep

size_SidesOfTriangle= ['None']*3               # Creating a blank list of size 3    

size_SidesOfTriangle[0]=float(input('\nPlease enter the size of the first side of your desired triangle : '))

while (size_SidesOfTriangle[0]<=0):            # Checking the size of the first side
    system('clear')                                 # Clearing the terminal 
    print('Error! the size of the sides of triangle can not be negative or zero please try again...')
    sleep(3.5)                                      # Stopping Terminal for three seconds
    system('clear')                                 # Clearing the terminal
    size_SidesOfTriangle[0]=float(input('Please enter the size of the first side of your desired triangle : '))

size_SidesOfTriangle[1]=float(input('\nPlease enter the size of the second side of your desired triangle : '))
    
while (size_SidesOfTriangle[1]<=0):            # Checking the size of the second side
    system('clear')                                 # Clearing the terminal
    print('Error! the size of the sides of triangle can not be negative or zero please try again...')
    sleep(3.5)                                      # Stopping Terminal for three seconds
    system('clear')                                 # Clearing the terminal
    print('Please enter the size of the first side of your desired triangle : ', size_SidesOfTriangle[0])
    size_SidesOfTriangle[1]=float(input('\nPlease enter the size of the second side of your desired triangle : '))

size_SidesOfTriangle[2]=float(input('\nPlease enter the size of the third side of your desired triangle : '))

while (size_SidesOfTriangle[2]<=0) :            # Checking the size of the third side
    system('clear')                             # Clearing the terminal
    print('Error! the size of the sides of triangle can not be negative or zero please try again...')
    sleep(3.5)                                  # Stopping Terminal for three seconds
    system('clear')                             # Clearing the terminal
    print('Please enter the size of the first side of your desired triangle : ', size_SidesOfTriangle[0])
    print('\nPlease enter the size of the second side of your desired triangle : ', size_SidesOfTriangle[1])
    size_SidesOfTriangle[2]=float(input('\nPlease enter the size of the third side of your desired triangle : '))
 
if (size_SidesOfTriangle[0]>(size_SidesOfTriangle[1]+size_SidesOfTriangle[2]) or size_SidesOfTriangle[1]>(size_SidesOfTriangle[0]+size_SidesOfTriangle[2]) or size_SidesOfTriangle[2]>(size_SidesOfTriangle[0]+size_SidesOfTriangle[1])): # checking the sides for make a triangle 
    flag=False
else:
    flag=True


if flag==False:
    system('clear')                             # Clearing the terminal
    print('You can not make a triangle\n')
elif flag==True:
    system('clear')                             # Clearing the terminal
    print('You can make a triangle\n')    
