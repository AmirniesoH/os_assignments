from os import system
from termcolor import colored

# Other Functions

def print_erorrs(theSentence, theColor):
    system('clear')
    print(colored(theSentence, theColor))
    input()
def calculate_fibonacciSequence(theSize, thefibonacciSequence):
    if theSize==0:
         thefibonacciSequence.pop()
    elif theSize!=1:
        for i in range(theSize-1):
            thefibonacciSequence.append(thefibonacciSequence[i]+thefibonacciSequence[i+1])

# Main Function

system('clear')

fibonacciSequence=[0, 1]

size=int(input('Please enter the desired size : '))

while(size<0):
    print_erorrs('The size can not be negative.Please try again...', 'red')
    system('clear')
    size=int(input('Please enter the desired size : '))

calculate_fibonacciSequence(size, fibonacciSequence)

system('clear')

print(colored('Fibonacci Sequence is equal to : ', 'green'),end='')

for i in range(len(fibonacciSequence)):
    print(fibonacciSequence[i], end='')
    if i!=len(fibonacciSequence)-1:
        print(colored(' ─ ','red'),end='')

input()
system('clear')