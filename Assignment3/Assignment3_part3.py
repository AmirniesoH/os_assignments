from os import system
from termcolor import colored

system('clear')
data=input('Please enter the desired sentence : ')

system('clear')
print('Your sentence has '+str(len(data.split()))+' words\n')
