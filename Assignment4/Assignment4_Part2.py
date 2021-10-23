from os import system
from termcolor import colored

# Other Functions

def print_table(theRow,theColumn):
    system('clear')

    print('\n'+'┌', end='')
    for i in range(theColumn):
        for j in range(3):
                print('─', end='')
        if i!=theColumn-1:        
            print('┬', end='')
        else:
            print('┐')

    for i in range(theRow):
        print('│', end='')
        for j in range(theColumn):    
                print('│'.rjust(4), end='')
        if i!=theRow-1:
            print('\n'+'├', end='')
            for j in range(theColumn):
                for k in range(3):
                    print('─', end='')
                if j!=theColumn-1:        
                    print('┼', end='')
                else:
                    print('┤') 

    print('\n'+'└', end='')
    for i in range(theColumn):
        for j in range(3):
                print('─', end='')
        if i!=theColumn-1:        
            print('┴', end='')
        else:
            print('┘')
def print_erorrs(theSentence, theColor):
    system('clear')
    print(colored(theSentence, theColor))
    input()

# Main Function

system('clear')

row=int(input('Please enter the size of the table row : '))

while(row<=0):
    print_erorrs('The row can not be zero or negative.Please try again...', 'red')
    system('clear')
    row=int(input('Please enter the size of the table row : '))

column=int(input('\nPlease enter the size of the table column : '))
    
while(column<=0):
    print_erorrs('The column can not be zero or negative.Please try again...', 'red')
    system('clear')
    print('Please enter the size of the table row : '+str(row))
    column=int(input('\nPlease enter the size of the table column : '))    

print_table(row, column)
input()
system('clear')