from os import system
from termcolor import colored

# Other Functions

def print_multiplicationTable(theRow, theColumn, theData):
    system('clear')

    print('\n'+'┌', end='')
    for i in range(theColumn):
        for j in range(5):
                print('─', end='')
        if i!=theColumn-1:        
            print('┬', end='')
        else:
            print('┐')

    for i in range(theRow):
        print('│', end='')
        for j in range(theColumn):  
            if i==0 or j==0:
                if (i==0) and (j==0):    
                    print(colored(str(theData[i][j]).rjust(3), 'red')+'│'.rjust(3), end='')
                else:
                    if len(str(theData[i][j]))==1:
                        print(colored(str(theData[i][j]).rjust(3), 'blue')+'│'.rjust(3), end='')
                    else:    
                        print(colored(str(theData[i][j]).rjust(len(str(theData[i][j]))+1), 'blue')+'│'.rjust(5-len(str(theData[i][j]))), end='')  
            else:
                if len(str(theData[i][j]))==1:
                        print(str(theData[i][j]).rjust(3)+'│'.rjust(3), end='')
                else:
                    print(str(theData[i][j]).rjust(len(str(theData[i][j]))+1)+'│'.rjust(5-len(str(theData[i][j]))), end='')
        if i!=theRow-1:
            print('\n'+'├', end='')
            for j in range(theColumn):
                for k in range(5):
                    print('─', end='')
                if j!=theColumn-1:        
                    print('┼', end='')
                else:
                    print('┤') 

    print('\n'+'└', end='')
    for i in range(theColumn):
        for j in range(5):
                print('─', end='')
        if i!=theColumn-1:        
            print('┴', end='')
        else:
            print('┘')
def print_erorrs(theSentence, theColor):
    system('clear')
    print(colored(theSentence, theColor))
    input()

def make_multiplicationTable(theRow, theColumn, theData):
    
    theData[0][0]='X'

    for i in range(row):
        theData[i+1][0]=i+1

    for j in range(column):
        theData[0][j+1]=j+1

    for i in range(row):
        for j in range(column):
            theData[i+1][j+1]=(i+1)*(j+1)

# Main Function

system('clear')

row=int(input('Please enter the size of the table row : '))

while row<=0 or row>526:
    print_erorrs('The row can not be zero or negative or bigger than 526. Please try again...', 'red')
    system('clear')
    row=int(input('Please enter the size of the table row : '))

column=int(input('\nPlease enter the size of the table column : '))
    
while column<=0 or column>19:
    print_erorrs('The column can not be zero or negative or bigger than 19. Please try again...', 'red')
    system('clear')
    print('Please enter the size of the table row : '+str(row))
    column=int(input('\nPlease enter the size of the table column : '))   
    

data=[[ '0' for i in range(column+1)]for j in range(row+1)]

make_multiplicationTable(row, column, data)

print_multiplicationTable(row+1, column+1, data)
input()
system('clear')