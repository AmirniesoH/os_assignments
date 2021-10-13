from termcolor import colored
from os import system
from random import randint


# Other Functions

def print_MenuOne():                # Print menu number one
    system('clear')

    print('\n╒══════════════════════════════════════════════╕')
    print('│                ➊ - Start Game                │')
    print('│                ➋ - Exit                      │')
    print('╘══════════════════════════════════════════════╛\n')

    theChoice=int(input('Please Choose your item : '))

    return(theChoice)

def print_MenuTwo():                # Print menu number two
    system('clear')

    print('╒══════════════════════════════════════════════╕')
    print('│              ➊ - Front of the hand           │')
    print('│              ➋ - Back of the hand            │')
    print('│              ➌ - Print Results               │')
    print('│              ➍ - Puase                       │')
    print('╘══════════════════════════════════════════════╛\n')

    theChoice=int(input('Please Choose your item : '))

    return(theChoice)

def print_MenuThree():              # Print menu number three
    system('clear')

    print('╒══════════════════════════════════════════════╕')
    print('│                 ➊ - Resume                   │')
    print('│                 ➋ - Replay                   │')
    print('│                 ➌ - Quit                     │')
    print('╘══════════════════════════════════════════════╛\n')

    theChoice=int(input('Please Choose your item : '))

    return(theChoice)

def play(theData):                  # Play
    randomNumberOne=randint(1, 2)
    randomNumberTwo=randint(1, 2)
    
    system('clear')

    if(randomNumberOne==1 and randomNumberTwo==1 and theData==1):
        print('Front(you) vs Front vs Front\n\nResult: ',colored('You drew :| ','blue'))
        input()
        return('Drew')
    elif(randomNumberOne==2 and randomNumberTwo==2 and theData==2):
        print('Back(you) vs Back vs Back\n\nResult: ',colored('You drew :| ','blue'))
        input()
        return('Drew')
    elif(randomNumberOne==1 and randomNumberTwo==2 and theData==1):
        print('Front(you) vs Front vs Back\n\nResult: ',colored('You won :| ','green'))
        input()
        return('Won')
    elif(randomNumberOne==1 and randomNumberTwo==2 and theData==2):
        print('Back(you) vs Front vs Back\n\nResult: ',colored('You won :| ','green'))
        input()
        return('Won') 
    elif(randomNumberOne==2 and randomNumberTwo==1 and theData==2):
        print('Back(you) vs Back vs Front\n\nResult: ',colored('You won :| ','green'))
        input()
        return('Won')      
    elif(randomNumberOne==2 and randomNumberTwo==1 and theData==1):
        print('Front(you) vs Back vs Front\n\nResult: ',colored('You won :| ','green'))
        input()
        return('Won')
    elif(randomNumberOne==1 and randomNumberTwo==1 and theData==2):
        print('Back(you) vs Front vs Front\n\nResult: ',colored('You lost :| ','red'))
        input()
        return('Lost')
    elif(randomNumberOne==2 and randomNumberTwo==2 and theData==1):
        print('Front(you) vs Back vs Back\n\nResult: ',colored('You lost :| ','red'))
        input()
        return('Lost')           


# Main Function

flagMenuOne=True

while flagMenuOne :
    choiceMenuOne=print_MenuOne()
    
    if choiceMenuOne==1 :       # Start the Game
        flagMenuTwo=True
        counter=0
        won=0
        drew=0
        lost=0

        while(flagMenuTwo and counter<5):
            choiceMenuTwo=print_MenuTwo()           
            flag=False                  # This flag is to print the result of the game

            if choiceMenuTwo==1:           
                counter+=1
                result=play(1)

                if result=='Won': 
                    won+=1

                elif result=='Lost':
                    lost+=1
                else:
                    drew+=1
            elif choiceMenuTwo==2:   
                counter+=1
                result=play(2)

                if result=='Won': 
                    won+=1
                elif result=='Lost':
                    lost+=1
                else:
                    drew+=1
            elif choiceMenuTwo==3:
                system('clear')
                print(colored('Won: '+str(won),'green'), '\n\n'+colored('Lost: '+str(lost),'red'), '\n\n'+colored('Drew: '+str(drew),'blue'), '\n\nPlayed :',str(won+lost+drew)+'/5')  
                input()       
            elif choiceMenuTwo==4:
                flagMenuThree=True 

                while (flagMenuThree):
                    choiceMenuThree=print_MenuThree()

                    if choiceMenuThree==1:
                        flagMenuThree=False
                    elif choiceMenuThree==2:
                        flagMenuThree=False
                        won=0
                        drew=0
                        lost=0
                        counter=0
                    elif choiceMenuThree==3:
                        flagMenuThree=False
                        flagMenuTwo=False 
                        flag=True
                    else :
                        system('clear')    
                        print('Your choice is false please try again...')
                        input()    

            else:
                system('clear')    
                print('Your choice is false please try again...')
                input() 
        if flag!=True:
            if (won>lost):
                system('clear')
                print(colored('You won the game :) ','green'))   
                input() 
            elif (lost>won):
                system('clear')
                print(colored('You lost the game :( ','red'))   
                input()
            else:
                system('clear')
                print(colored('You drew the game :| ','blue'))   
                input()         
    elif choiceMenuOne==2:          # Exit        
        flagMenuOne=False
        print('\n')  
    else:
        system('clear')    
        print('Your choice is false please try again...')
        input()   