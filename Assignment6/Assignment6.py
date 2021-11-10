from os import system
from termcolor import colored
#%%

def print_erorrs(theSentence, theColor):
    system('clear')
    print(colored(theSentence, theColor))
    input()

def print_Menu():
    system('clear')

    print('╒═══════════════════════════════════════════════════╕')
    print('│         ➊ - English to Persian translation        │')
    print('│         ➋ - Persian to Persian translation        │')
    print('│         ➌ - Add a new word to the word bank       │')
    print('│         ➍ - Save and Exit                         │')
    print('╘═══════════════════════════════════════════════════╛\n')

    Choice=int(input('Please Choose your item : '))

    return(Choice)

#%%

def read_File(thePath, theWordsBank):
    
    with open(thePath, 'r') as input_File:
        
        temp_Text=(input_File.read()).split('\n')
        
        for i in range(0,len(temp_Text),2):
            theWordsBank.append({'English':temp_Text[i], 'Persian':temp_Text[i+1]})

def write_File(thePath, theWordsBank):
    
    with open(thePath, 'tw') as output_File:

        for i in range(len(theWordsBank)):
            if i != len(theWordsBank)-1 :
                output_File.write('{0}\n{1}\n'.format(theWordsBank[i]['English'], theWordsBank[i]['Persian']))
            else:
                output_File.write('{0}\n{1}'.format(theWordsBank[i]['English'], theWordsBank[i]['Persian']))

#%%

def search_EnglishWord(theWordsBank, theWord):
    for i in range(len(theWordsBank)):
        if theWordsBank[i]['English']== theWord:
            return i
    return -1

def search_PersianWord(theWordsBank, theWord):
    for i in range(len(theWordsBank)):
        if theWordsBank[i]['Persian']== theWord:
            return i
    return -1

#%%

def insert(theWordsBank):
    english_Word = (input('Please enter your desired word in English : ')).lower()
    
    while search_EnglishWord(theWordsBank, english_Word) != -1:
        print_erorrs("""'{}' is in the words bank""".format(english_Word), 'red')
        
        system('clear')
        english_Word = input('Please enter your desired word in English : ')
    while not (english_Word and not english_Word.isspace()):
        print_erorrs('The word must contain numbers or letters', 'red')
        
        system('clear')
        english_Word = input('Please enter your desired word in English : ')
    persian_Word = (input('\nPlease enter your desired word in Persain : ')).lower()

    while search_PersianWord(theWordsBank, persian_Word) != -1:
        print_erorrs("""'{}' is in the words bank""".format(persian_Word), 'red')
    
        system('clear')
        print('Please enter your desired word in English : {}'.format(english_Word))
        persian_Word = input('\nPlease enter your desired word in Persian : ')
    while not (persian_Word and not persian_Word.isspace()):
        print_erorrs('The word must contain numbers or letters', 'red')
        
        system('clear')
        print('Please enter your desired word in English : {}'.format(english_Word))
        persian_Word = input('\nPlease enter your desired word in Persian : ')
    theWordsBank.append({'English':english_Word, 'Persian':persian_Word})

#%%

def translate_EnglishToPersian(theWordsBank, theEnglish_Text):
    
    persian_Sentence =''

    for i in range(len(theEnglish_Text)):
        for word in theEnglish_Text[i].split(' '):

            theIndex = search_EnglishWord(theWordsBank, word)

            if theIndex == -1 :
                persian_Sentence += word
            else:
                persian_Sentence += theWordsBank[theIndex]['Persian']   

            persian_Sentence += ' '     

        temp = list(persian_Sentence)
        temp[-1]='.'
        persian_Sentence = ''.join(temp)

    return persian_Sentence
        
def translate_PerianToEnglish(theWordsBank, thePersian_Text):
    
    english_Sentence =''

    for i in range(len(thePersian_Text)):
        for word in thePersian_Text[i].split(' '):

            theIndex = search_PersianWord(theWordsBank, word)

            if theIndex == -1 :
                english_Sentence += word
            else:
                english_Sentence += theWordsBank[theIndex]['English']   

            english_Sentence += ' '     

        temp = list(english_Sentence)
        temp[-1]='.'
        english_Sentence = ''.join(temp) 

    return english_Sentence

#%%

wordsBank=[]

try:
    read_File('words_Bank.txt', wordsBank)
except FileNotFoundError:
    print_erorrs('File is not created...', 'red')
finally:

    while True:
        choice_Menu=print_Menu()

        match choice_Menu:
            case 1:
                system('clear')
                english_Text = (input('Please enter your desired text in English : ')).split('.')

                print('\nPersian : '+translate_EnglishToPersian(wordsBank, english_Text))
                input()
            case 2:
                system('clear')
                persian_Text = (input('Please enter your desired text in Persian : ')).split('.')

                print('\nEnglish : '+translate_PerianToEnglish(wordsBank, persian_Text))
                input()

            case 3:
                system('clear')
                insert(wordsBank)
            case 4:
                try:
                    write_File('words_Bank.txt', wordsBank)
                except FileNotFoundError:
                    print_erorrs('File is not created...', 'red')
                finally:
                    break
            case _:
                print_erorrs('Erorr! Your choice is false. Please try again...','red')

system('clear')