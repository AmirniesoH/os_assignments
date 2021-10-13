from datetime import timedelta
from os import system
from termcolor import colored


# Other Function

def print_MenuOne():
    system('clear')

    print('╒══════════════════════════════════════════════╕')
    print('│                  ➊ - Start                   │')
    print('│                  ➋ - Exit                    │')
    print('╘══════════════════════════════════════════════╛\n')

    theChoice=int(input('Please Choose your item : '))

    return(theChoice)

def print_MenuTwo():                # Print menu number two
    system('clear')

    print('╒══════════════════════════════════════════════╕')
    print('│                ➊ - Hour                      │')
    print('│                ➋ - Minute                    │')
    print('│                ➌ - Seconds                   │')
    print('│                ➍ - print the time            │')
    print('│                ➎ - Back Pgae                 │')
    print('╘══════════════════════════════════════════════╛\n')

    theChoice=int(input('Please Choose your item : '))

    return(theChoice)    

def convert_TimeToSeconds(theHours, theMinutes, theSeconds):
    return((theHours*3600)+(theMinutes*60)+theSeconds)


# Main Function 


flagMenuOne=True
flagHour=False
flagMinute=False
flagSeconds=False
time={'hour':0,'minute':0,'seconds':0}

while(flagMenuOne):
    choiceMenuOne=print_MenuOne()

    if(choiceMenuOne==1):
        flagMenuTwo=True
        flagHour=True

        while(flagMenuTwo):
            choiceMenuTwo=print_MenuTwo()

            if(choiceMenuTwo==1):
                system('clear')
                hour=int(input('please enter the hour : '))

                if(hour<0 or hour>23):
                    system('clear')
                    print(colored('Erorr! the hour can not be negative or bigger than 23...', 'red'))
                    input()
                else:
                    time['hour']=hour
            elif(choiceMenuTwo==2):
                system('clear')
                minute=int(input('please enter the minute : '))

                if(minute<0 or minute>=60):
                    system('clear')
                    print(colored('Erorr! the minute can not be negative or begger than 60...', 'red'))
                    input()
                else:
                    time['minute']=minute
            elif(choiceMenuTwo==3):
                system('clear')
                seconds=int(input('please enter the seconds : '))

                if(seconds<0 or seconds>=60):
                    system('clear')
                    print(colored('Erorr! the seconds can not be negative or bigger than 60...', 'red'))
                    input()
                else:
                    time['seconds']=seconds
            elif(choiceMenuTwo==4):
                system('clear')
                bufOne=convert_TimeToSeconds(time['hour'], time['minute'], time['seconds'])
                bufTwo=str(timedelta(seconds=bufOne))
                print(bufTwo+' is equal to '+str(bufOne)+' seconds')   
                input()    
            elif(choiceMenuTwo==5):
                flagMenuTwo=False
            else:
                system('clear')    
                print('Your choice is false please try again...')
                input() 
    elif(choiceMenuOne==2):
        flagMenuOne=False            
    else:
        system('clear')    
        print('Your choice is false please try again...')
        input()      