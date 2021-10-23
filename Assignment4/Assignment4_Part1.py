from os import system
from random import choice
from termcolor import colored
from timeit import default_timer

# Other Funtions

def print_MenuOne():                       
    system('clear')

    print('╒══════════════════════════════════════════════╕')
    print('│                ➊ - Start Game                │')
    print('│                ➋ - Exit                      │')
    print('╘══════════════════════════════════════════════╛\n')

    theChoice=int(input('Please Choose your item : '))

    return(theChoice)
def print_MenuTwo():
    system('clear')

    print('╒══════════════════════════════════════════════╕')
    print('│           ➊ - Play with out computer         │')
    print('│           ➋ - play with computer             │')
    print('│           ➌ - Back Page                      │')
    print('╘══════════════════════════════════════════════╛\n')

    theChoice=int(input('Please Choose your item : '))

    return(theChoice)
def print_gameErorrs(theSentence, theColor):
    system('clear')
    print(colored(theSentence, theColor))
    input()
def print_boardGame(theRow,theColumn, theBoard):
    system('clear')

    print('\n'+'┌'.rjust(31), end='')
    for i in range(theColumn):
        for j in range(3):
                print('─', end='')
        if i!=theColumn-1:        
            print('┬', end='')
        else:
            print('┐')

    for i in range(theRow):
        print('│'.rjust(31), end='')
        for j in range(theColumn):
            if theBoard[i][j]=='𝞦':
                print(colored(str(theBoard[i][j]).rjust(2),'blue')+'│'.rjust(2), end='')
            elif theBoard[i][j]=='𝞞':
                print(colored(str(theBoard[i][j]).rjust(2),'red')+'│'.rjust(2), end='')
            else:    
                print(str(theBoard[i][j]).rjust(2)+'│'.rjust(2), end='')
        if i!=theRow-1:
            print('\n'+'├'.rjust(31), end='')
            for j in range(theColumn):
                for k in range(3):
                    print('─', end='')
                if j!=theColumn-1:        
                    print('┼', end='')
                else:
                    print('┤') 

    print('\n'+'└'.rjust(31), end='')
    for i in range(theColumn):
        for j in range(3):
                print('─', end='')
        if i!=theColumn-1:        
            print('┴', end='')
        else:
            print('┘')

def isWinner(theRow, theColumn, theBoard, theSign):
    counter=[0, 0, 0, 0]

    for i in range(theRow):
        counter[0]=0
        counter[1]=0
        for j in range(theColumn):
            if theBoard[i][j]==theSign:
                counter[0]+=1
            if theBoard[j][i]==theSign:
                counter[1]+=1
        if theBoard[i][i]==theSign:
            counter[2]+=1
        if theBoard[i][2-i]==theSign:
            counter[3]+=1

        if 3 in counter:
            return True
    return False                        
def check_playerSelection(theBoard, thePlayerInput, theSign):
    match thePlayerInput:
        case 1:
            if (theBoard[0][0] != '𝞦' and theBoard[0][0] != '𝞞'):
                theBoard[0][0]=theSign
                return True
            else:
                print_gameErorrs('Erorr! this place is fill please try again...', 'red')
                return False
                
        case 2:
            if (theBoard[0][1] != '𝞦' and theBoard[0][1] != '𝞞'):
                theBoard[0][1]=theSign
                return True
            else:
                print_gameErorrs('Erorr! this place is fill please try again...', 'red')
                return False
        case 3:
            if (theBoard[0][2] != '𝞦' and theBoard[0][2] != '𝞞'):
                theBoard[0][2]=theSign
                return True
            else:
                print_gameErorrs('Erorr! this place is fill please try again...', 'red')
                return False
        case 4:
            if (theBoard[1][0] != '𝞦' and theBoard[1][0] != '𝞞'):
                theBoard[1][0]=theSign
                return True
            else:
                print_gameErorrs('Erorr! this place is fill please try again...', 'red')
                return False
        case 5:
            if (theBoard[1][1] != '𝞦' and theBoard[1][1] != '𝞞'):
                theBoard[1][1]=theSign
                return True
            else:
                print_gameErorrs('Erorr! this place is fill please try again...', 'red')
                return False
        case 6:
            if (theBoard[1][2] != '𝞦' and theBoard[1][2] != '𝞞'):
                theBoard[1][2]=theSign
                return True
            else:
                print_gameErorrs('Erorr! this place is fill please try again...', 'red')
                return False
        case 7:
            if (theBoard[2][0] != '𝞦' and theBoard[2][0] != '𝞞'):
                theBoard[2][0]=theSign
                return True
            else:
                print_gameErorrs('Erorr! this place is fill please try again...', 'red')
                return False
        case 8:
            if (theBoard[2][1] != '𝞦' and theBoard[2][1] != '𝞞'):
                theBoard[2][1]=theSign
                return True
            else:
                print_gameErorrs('Erorr! this place is fill please try again...', 'red')
                return False
        case 9:
            if (theBoard[2][2] != '𝞦' and theBoard[2][2] != '𝞞'):
                theBoard[2][2]=theSign
                return True
            else:
                print_gameErorrs('Erorr! this place is fill please try again...', 'red')
                return False
        case _:
            print_gameErorrs('Erorr! this place is fill please try again...', 'red')
            return False  

def play(theBoard):
    counter=0

    while(True):

        print_boardGame(3, 3, theBoard) 

        playerOne=int(input('\n\nPlease enter your desired number according to the table above (Player One): '))
        
        while(check_playerSelection(theBoard, playerOne, '𝞦')==False):
            print_boardGame(3, 3, theBoard) 
            playerOne=int(input('\n\nPlease enter your desired number according to the table above (Player One): '))

        if isWinner(3, 3, theBoard, '𝞦'):
            print_gameErorrs('Player One Wins :)', 'green')
            break
        elif counter==8:
            print_gameErorrs('player one and Player Two draw :|', 'white')
            break

        counter+=1
        
        print_boardGame(3 ,3, theBoard)

        playerTwo=int(input('\n\nPlease enter your desired number according to the table above (Player Two): '))

        while (check_playerSelection(theBoard, playerTwo, '𝞞')==False):
            print_boardGame(3 ,3, theBoard)
            playerTwo=int(input('\n\nPlease enter your desired number according to the table above (Player Two): '))

        if isWinner(3, 3, theBoard, '𝞞'):
            print_gameErorrs('Player Two Wins :)', 'green')
            break

        counter+=1
def play_withComputer(theBoard):
    counter=0
    computer=[1, 2, 3, 4, 5, 6, 7, 8, 9] 

    while(True):

        print_boardGame(3, 3, theBoard) 

        playerOne=int(input('\n\nPlease enter your desired number according to the table above (Player One): '))
        
        while(check_playerSelection(theBoard, playerOne, '𝞦')==False):
            print_boardGame(3, 3, theBoard) 
            playerOne=int(input('\n\nPlease enter your desired number according to the table above (Player One): '))

        if isWinner(3, 3, theBoard, '𝞦'):
            print_gameErorrs('You Win :)', 'green')
            break
        elif counter==8:
            print_gameErorrs('You and computer draw :|', 'white')
            break

        counter+=1

        computer.pop(computer.index(playerOne))

        check_playerSelection(theBoard, choice(computer), '𝞞')
            
        if isWinner(3, 3, theBoard, '𝞞'):
            print_gameErorrs('You Lost :(', 'red')
            break

        counter+=1


# Main Function

while(True):
    choiceMenuOne=print_MenuOne()

    match choiceMenuOne:
        case 1:
            while(True):
                choiceMenuTwo=print_MenuTwo()
                board=[['𝟙', '𝟚', '𝟛'], ['𝟜', '𝟝', '𝟞'], ['𝟟', '𝟠', '𝟡']]
                match choiceMenuTwo:
                    case 1:
                        start=default_timer()
                        play(board)
                        stop=default_timer()
                        print_gameErorrs('Time : '+str(stop-start), 'white')
                    case 2:
                        start=default_timer()
                        play_withComputer(board)
                        stop=default_timer()
                        print_gameErorrs('Time : '+str(stop-start), 'white')
                    case 3:
                        break
                    case _:
                        print_gameErorrs('Erorr! Your choice is false. Please try again...','red')        
        case 2:
            system('clear')
            exit()
        case _:
            print_gameErorrs('Erorr! Your choice is false. Please try again...','red')        