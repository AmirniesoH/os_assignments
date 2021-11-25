from os import system
import time
from termcolor import colored


class Time:
    def __init__(self, theHour=0, theMinute=0, theSecond=0):
        self.hour=theHour
        self.minute=theMinute
        self.second=theSecond
    
    def set_hour(self, theHour):
        self.hour=theHour

    def set_minute(self, theMinute):
        self.minute=theMinute

    def set_second(self, theSecond):
        self.second=theSecond

    def __add__(self, theObject):
        second=self.second+theObject.second
        minute=self.minute+theObject.minute
        hour=self.hour+theObject.hour
        if second//60 > 0:
            minute+=second//60
            second = second%60
        if minute//60>0:
            hour+=minute//60
            minute=minute%60
        if hour > 23:
            hour=hour%24
        return Time(hour, minute, second)
    
    def __sub__(self, theObject):
        second=self.second-theObject.second
        minute=self.minute-theObject.minute
        hour=self.hour-theObject.hour
        if second< 0:
            minute-=1
            second+=60
        if minute<0:
            hour-=1
            minute+=60
        if hour < 0:
            hour+=24
        return Time(hour, minute, second)
    
        
        return Time(hour, minute, second)
    
    def convert_SecondToTime(self, theSecond):
        self.second = theSecond % (24 * 3600)
        self.hour = self.second // 3600
        self.second %= 3600
        self.minute = self.second // 60
        self.second %= 60
    
    def convert_TimeToSecond(self):
        seconds= ( self.hour * 3600) + (self.minute * 60) + self.second
        return seconds
    def input_console(self, theKey):
        self.hour=int(input('Please enter your desired {} hour : '.format(theKey)))
        while self.hour>=24 or self.hour<0:
            system('clear')
            print(colored('the hour must be between 0 and 24', 'red'))
            input()
            system('clear')
            self.hour=int(input('Please enter your desired {} hour : '.format(theKey)))
        
        self.minute=int(input('\nPlease enter your desired {} minute : '.format(theKey)))
        while self.minute>=60 or self.minute<0:
            system('clear')
            print(colored('the minute must be between 0 and 60', 'red'))
            input()
            system('clear')
            print('Please enter your desired {} hour : {} '.format(theKey, self.hour))
            self.minute=int(input('\nPlease enter your desired {} minute : '.format(theKey)))
        
        self.second=int(input('\nPlease enter your desired {} second : '.format(theKey)))
        while self.second>=60 or self.second<0:
            system('clear')
            print(colored('the second must be between 0 and 60', 'red'))
            input()
            system('clear')
            print('Please enter your desired {} hour : {} '.format(theKey, self.hour))
            print('\nPlease enter your desired {} minute : {}'.format(theKey, self.minute))
            self.second=int(input('\nPlease enter your desired {} second : '.format(theKey)))
        
    def print_CoordinatedUniversalTime(self):
        print('%02d : %02d : %02d'%(self.hour, self.minute, self.second), end='')

def print_MainMenu():
    system('clear')

    print('╒══════════════════════════════════════════════╕')
    print('│              ➊ - Addition                    │')
    print('│              ➋ - Minus                       │')
    print('│              ➌ - Seconds to time             │')
    print('│              ➍ - Time to seconds             │')
    print('│              ➎ - Exit                        │')
    print('╘══════════════════════════════════════════════╛\n')

    Choice=int(input('Please Choose your item : '))

    return(Choice)

def print_message(theSentence, theColor):                
    system('clear')
    print(colored(theSentence, theColor))
    input()

timeOne = Time()
timeTwo = Time()
result = Time()

while True:
    choice_MainMenu=print_MainMenu()

    match choice_MainMenu:
        case 1:
            system('clear')
            timeOne.input_console('first')
            system('clear')
            timeTwo.input_console('The second')
            result=timeOne+timeTwo
            system('clear')
            print('( ',end='')
            timeOne.print_CoordinatedUniversalTime()
            print(' )',end='')
            print(' + ', end='')
            print('( ',end='')
            timeTwo.print_CoordinatedUniversalTime()
            print(' )',end='')
            print(' = ', end='')
            result.print_CoordinatedUniversalTime()
            input()
        case 2:
            system('clear')
            timeOne.input_console('first')
            system('clear')
            timeTwo.input_console('The second')
            result=timeOne-timeTwo
            system('clear')
            print('( ',end='')
            timeOne.print_CoordinatedUniversalTime()
            print(' )',end='')
            print(' - ', end='')
            print('( ',end='')
            timeTwo.print_CoordinatedUniversalTime()
            print(' )',end='')
            print(' = ', end='')
            result.print_CoordinatedUniversalTime()
            input()
        case 3:
            system('clear')
            seconds=int(input('Please enter your desired seconds : '))
            timeOne.convert_SecondToTime(seconds)
            system('clear')
            print('{} seconds is equal to '.format(seconds), end='') 
            timeOne.print_CoordinatedUniversalTime()
            input()
        case 4:
            system('clear')
            timeOne.input_console('')
            system('clear')
            timeOne.print_CoordinatedUniversalTime()
            print(' is equal to {} seconds'.format(timeOne.convert_TimeToSecond()))
            input()
        case 5:
            system('clear')
            break
        case _:
            print_message('Erorr! Your choice is incorrect. Please try again...','red')


               
        