from datetime import timedelta
from os import system
from termcolor import colored


# Other Function

def print_Menu():
    system('clear')

    print('╒══════════════════════════════════════════════╕')
    print('│                  ➊ - Start                   │')
    print('│                  ➋ - Exit                    │')
    print('╘══════════════════════════════════════════════╛\n')

    theChoice=int(input('Please Choose your item : '))

    return(theChoice)

def convert_SecondsToTime(theSeconds):
    return(timedelta(seconds=theSeconds))

# Main Function

flagMenu=True

while(flagMenu):
    choiceMenu=print_Menu()

    if(choiceMenu==1):
        system('clear')
        seconds=float(input('Please enter the time in seconds : '))
        
        if(seconds<0):
            system('clear')
            print(colored('Erorr! the seconds can not be negative...', 'red'))
            input()
        else:
            system('clear')
            print(str(seconds)+' seconds is equal to '+str(convert_SecondsToTime(seconds))) 
            input()
    elif(choiceMenu==2):
        flagMenu=False    
    else:
        system('clear')    
        print('Your choice is false please try again...')
        input() 