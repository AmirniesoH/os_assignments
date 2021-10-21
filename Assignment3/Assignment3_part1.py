from os import system
from random import choice, randint
from termcolor import colored

# other Functions ----------

def print_Menu():                # Print menu number one
    system('clear')

    print('╒══════════════════════════════════════════════╕')
    print('│                ➊ - Start Game                │')
    print('│                ➋ - Exit                      │')
    print('╘══════════════════════════════════════════════╛\n')

    theChoice=int(input('Please Choose your item : '))

    return(theChoice)


# Main Function ------------  


flagMenu=True

wordsBank=['apple', 'banana', 'cherry', 'python' , 'java script', 'blue', 'football', 'esteghlal']
correctGuessesOfTheUser=[]

while(flagMenu):
    choiceMenu=print_Menu()

    match choiceMenu:
        case 1:
            numberOfMistakes=0
            selectedWord=choice(wordsBank)
            while(True):
                system('clear')
                counter=0

                for i in range(len(selectedWord)):
                    if (selectedWord[i] in correctGuessesOfTheUser):
                        print(selectedWord[i], end=' ')
                        counter+=1
                    elif (selectedWord[i]==' '):
                        print(' ', end=' ')
                        counter+=1
                    else:
                        print('_', end=' ')

                if (counter==len(selectedWord)):
                    input()
                    system('clear')
                    print(colored('You Win :)', 'green'))
                    input()
                    break
                guessesOfTheUser=input('\n\nPlease guess a character of the word (The number of your chances = '+str(6-numberOfMistakes)+') : ')

                while(len(guessesOfTheUser)>=2 or len(guessesOfTheUser)==0 or guessesOfTheUser==' ' ):
                    system('clear')
                    print(colored('Erorr! Your input is incorrect. Please try again...','red'))
                    input()
                    system('clear')
                    for i in range(len(selectedWord)):
                        if (selectedWord[i] in correctGuessesOfTheUser):
                            print(selectedWord[i], end=' ')
                        elif (selectedWord[i]==' '):
                            print(' ', end=' ')
                        else:
                            print('_', end=' ')          
                    guessesOfTheUser=input('\n\nPlease guess a character of the word (The number of your chances = '+str(6-numberOfMistakes)+') : ')
                if (guessesOfTheUser in correctGuessesOfTheUser):
                    system('clear')
                    print(colored('Your guess is repetitive :|', 'blue'))
                    input()
                elif (guessesOfTheUser in selectedWord):
                    correctGuessesOfTheUser.append(guessesOfTheUser)
                    system('clear')
                    print(colored('Correct :)', 'green'))
                    input()
                else:
                    system('clear')
                    print(colored('Incorrect :(', 'red'))
                    input()
                    numberOfMistakes+=1

                if numberOfMistakes==6:
                    system('clear')
                    print(colored('You Lost :(', 'red'))
                    input()
                    break  
                  
        case 2:
            flagMenu=False
        case _:
            system('clear')
            print(colored('Erorr! Your choice is false. Please try again...','red'))
            input()