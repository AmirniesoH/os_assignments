from os import system
from termcolor import colored

#%%
def print_erorrs(theSentence, theColor):
    system('clear')
    print(colored(theSentence, theColor))
    input()

def print_MainMenuOne():
    system('clear')

    print('╒══════════════════════════════════════════════╕')
    print('│                ➊ - Insert                    │')
    print('│                ➋ - Remove                    │')
    print('│                ➌ - Edit                      │')
    print('│                ➍ - Next Page                 │')
    print('│                ➎ - Save and Exit             │')
    print('╘══════════════════════════════════════════════╛\n')

    Choice=int(input('Please Choose your item : '))

    return(Choice)

def print_MainMenuTwo():
    system('clear')

    print('╒══════════════════════════════════════════════╕')
    print('│            ➊ - Buy                           │')
    print('│            ➋ - Print Purchase Invoice        │')
    print('│            ➌ - ‌Back Page                     │')
    print('╘══════════════════════════════════════════════╛\n')

    Choice=int(input('Please Choose your item : '))

    return(Choice)

def print_SubMenu():
    system('clear')

    print('╒═════════════════════════════════════════════╕')
    print('│                ➊ - Code                     │')
    print('│                ➋ - Price                    │')
    print('│                ➌ - Inventory                │')
    print('│                ➍ - Back Page                │')
    print('╘═════════════════════════════════════════════╛\n')

    Choice=int(input('Please Choose your item : '))

    return(Choice)

def print_PurchaseInvoice(theRow, theColumn, theShoppingCart, theTitle, theTotal):
    system('clear')

    print('\n'+'┌', end='')
    for i in range(theColumn):
        for j in range(len(theTitle[i])+2):
                print('─', end='')
        if i!=theColumn-1:        
            print('┬', end='')
        else:
            print('┐')

    for i in range(theRow):
        print('│', end='')
        for j in range(theColumn):  
            if i==0 :
                print(colored(str(theTitle[j]).rjust(len(theTitle[j])+1), 'blue')+'│'.rjust(2), end='')
            else:
                if j == 0:
                    print(colored(str(i).rjust(3), 'white')+'│'.rjust(4), end='')
                elif j==1:
                   print(str(theShoppingCart[i-1]['ProductName']).rjust( int(( len(theTitle[j])+2 - len(theShoppingCart[i-1]['ProductName']) )/2 ) + len(theShoppingCart[i-1]['ProductName']) ) + '│'.rjust( len(theTitle[j])+2 - ( int(( len(theTitle[j])+2 - len(theShoppingCart[i-1]['ProductName']) )/2 ) + len(theShoppingCart[i-1]['ProductName']) ) +1), end='')
                elif j==2:
                   print(str(theShoppingCart[i-1]['Quantity']).rjust( int(( len(theTitle[j])+2 - len(str(theShoppingCart[i-1]['Quantity'])) )/2 ) + len(str(theShoppingCart[i-1]['Quantity'])) ) + '│'.rjust( len(theTitle[j])+2 - ( int(( len(theTitle[j])+2 - len(str(theShoppingCart[i-1]['Quantity'])) )/2 ) + len(str(theShoppingCart[i-1]['Quantity'])) ) +1), end='')
                elif j==3: 
                   print(str(theShoppingCart[i-1]['Price']).rjust( int(( len(theTitle[j])+2 - len(str(theShoppingCart[i-1]['Price'])) )/2 ) + len(str(theShoppingCart[i-1]['Price'])) ) + '│'.rjust( len(theTitle[j])+2 - ( int(( len(theTitle[j])+2 - len(str(theShoppingCart[i-1]['Price'])) )/2 ) + len(str(theShoppingCart[i-1]['Price'])) ) +1), end='')
                else:
                   print(str(theShoppingCart[i-1]['Cost']).rjust( int(( len(theTitle[j])+2 - len(str(theShoppingCart[i-1]['Cost'])) )/2 ) + len(str(theShoppingCart[i-1]['Cost'])) ) + '│'.rjust( len(theTitle[j])+2 - ( int(( len(theTitle[j])+2 - len(str(theShoppingCart[i-1]['Cost'])) )/2 ) + len(str(theShoppingCart[i-1]['Cost'])) ) +1), end='')
        if i!=theRow-1:
            print('\n'+'├', end='')
            for j in range(theColumn):
                for k in range(len(theTitle[j])+2):
                    print('─', end='')
                if j!=theColumn-1:        
                    print('┼', end='')
                else:
                    print('┤') 
    print('\n'+'└', end='')
    for i in range(theColumn):
        for j in range(len(theTitle[i])+2):
                print('─', end='')
        if i!=theColumn-1:        
            print('┴', end='')
        else:
            print('┘')

    print('\n'+'┌', end='')
    for i in range(2):
        for j in range(7):
                print('─', end='')
        if i!=1:        
            print('┬', end='')
        else:
            print('┐')
    
    for i in range(1):
        print('│', end='')
        for j in range(2):
            if j==0:  
                print(colored('Total'.rjust(6), 'blue') + '│'.rjust(2), end='')
            else:
                print(str(theTotal).rjust( int( (7 - len(str(theTotal)) ) /2 ) + len(str(theTotal)) ) + '│'.rjust( 7 - ( int(( 7 - len(str(theTotal)) )/2 ) + len(str(theTotal)) ) +1), end='')
        if i!=0:
            print('\n'+'├', end='')
            for j in range(2):
                for k in range(7):
                    print('─', end='')
                if j!=1:        
                    print('┼', end='')
                else:
                    print('┤') 
    print('\n'+'└', end='')
    for i in range(2):
        for j in range(7):
                print('─', end='')
        if i!=1:        
            print('┴', end='')
        else:
            print('┘')
#%%
def read_File(thePath, theProduction):

    with open(thePath, 'r') as input_file:
        for row in input_file:
            temp_information = row[:-1].split(',')
            theProduction.append({'Code' : temp_information[0], 'ProductName' : temp_information[1], 'Price' : int(temp_information[2]), 'Inventory' : int(temp_information[3])})

def write_File(thePath, theProduction):

    with open(thePath, 'tw') as output_file:
        for row in theProduction:
            output_file.write(row['Code']+','+row['ProductName']+',{},{}\n'.format(row['Price'], row['Inventory']))

#%%
def search_CodeInProduction(theCode, theProduction):
    for i in range(len(theProduction)):
        if theCode == theProduction[i]['Code']:
            return i
    return -1        

def search_ProductNameInProduction(theProductName, theProduction):
    for i in range(len(theProduction)):
        if theProductName == theProduction[i]['ProductName']:
            return i
    return -1

def search_ProductNameInShoppingCart(theSoppingCart, theProductName):
    for i in range(len(theSoppingCart)):
        if theProductName == theSoppingCart[i]['ProductName']:
            return i
    return -1    
    
#%%
def insert(theProduction):
    system('clear')
    temp_Code = input('Please enter the code : ')

    while search_CodeInProduction(temp_Code, theProduction) != -1:
        print_erorrs('Erorr! The code entered is duplicate.Please try again...', 'red')
        system('clear')
        temp_Code = input('Please enter the code : ')

    temp_ProductName = input('\nPlease enter the product name : ')

    while search_ProductNameInProduction(temp_ProductName, theProduction) != -1:
        print_erorrs('Erorr! The product name entered is duplicate.Please try again...', 'red')
        system('clear')
        print('Please enter the code : {}'.format(temp_Code))
        temp_ProductName = input('\nPlease enter the product name : ')

    temp_Price = int(input('\nPlease enter the Price : '))   

    while temp_Price<=0:
        print_erorrs('Erorr! The price entered can not be zero or negative.Please try again...', 'red')
        system('clear')
        print('Please enter the Code : {}'.format(temp_Code))
        print('\nPlease enter the Product Name : {}'.format(temp_ProductName))
        temp_Price = int(input('\nPlease enter the Price : '))

    temp_Inventory = int(input('\nPlease enter the Inventory : '))

    while temp_Inventory<0:
        print_erorrs('Erorr! The Inventory entered can not be zero or negative.Please try again...', 'red')
        system('clear')
        print('Please enter the Code : {}'.format(temp_Code))
        print('\nPlease enter the Product Name : {}'.format(temp_ProductName))
        print('\nPlease enter the Price : {}'.format(temp_Price))
        temp_Inventory = int(input('\nPlease enter the Inventory'))

    theProduction.append({'Code' : temp_Code, 'ProductName' : temp_ProductName, 'Price' : temp_Price, 'Inventory' : temp_Inventory})
        
def remove(theProduction, theIndex):
    if theIndex == -1:
        print_erorrs('Erorr! The code or product name entered is incorrect.Please try again...', 'red')
    else:    
        theProduction.pop(theIndex)

def edit(theProduction, theIndex):
    if theIndex == -1:
        print_erorrs('Erorr! the product name entered is incorrect.Please try again...', 'red')
    else:
        while True:
            choice_SumMenu = print_SubMenu()

            match choice_SumMenu:
                case 1:
                    system('clear')
                    temp_code = input('please enter the desired code : ')
                    theProduction[theIndex]['Code'] = temp_code
                case 2:
                    system('clear')
                    temp_price = int(input('Please enter the desired price in dollars : '))

                    while temp_price <= 0:
                       print_erorrs('Erorr! The price entered can not be zero or negative.Please try again...', 'red')
                       system('clear')
                       temp_price = int(input('Please enter the desired price in dollars : '))

                    theProduction[theIndex]['Price'] = temp_price
                case 3:
                    system('clear')
                    temp_Inventory = int(input('Please enter the Inventory : '))

                    while temp_Inventory < 0:
                       print_erorrs('Erorr! The Inventory entered can not negative.Please try again...', 'red')
                       system('clear')
                       temp_Inventory = int(input('Please enter the Inventory : '))

                    theProduction[theIndex]['Inventory']=temp_Inventory
                case 4:
                    break   
                case _:
                    print_erorrs('Erorr! Your choice is false. Please try again...','red')

def buy(theProduction, theShoppingCart , theIndex_Production):
    if theIndex_Production == -1:
        print_erorrs('Erorr! the product name entered is incorrect.Please try again...', 'red')
    else:
        system('clear')
        quantity = int(input('Please enter the desired quantity : '))

        if quantity <=0 :
            print_erorrs('Erorr! quantity can not be zero or negative.Please try again...', 'red')
        elif quantity > theProduction[theIndex_Production]['Inventory']:
            print_erorrs('Lack of inventory', 'red')
        else:
            Index_SoppingCart = search_ProductNameInShoppingCart(theShoppingCart, theProduction[theIndex_Production]['ProductName'])
            
            if Index_SoppingCart != -1:
                theShoppingCart[Index_SoppingCart]['Quantity']=quantity
            else:    
                theShoppingCart.append({'ProductName' : theProduction[theIndex_Production]['ProductName'], 'Price' : theProduction[theIndex_Production]['Price'], 'Quantity' : quantity, 'Cost' : quantity*theProduction[theIndex_Production]['Price']})

#%%
def calculate_TotalCost(theShoppingCart):
    totalCost=0

    for row in theShoppingCart:
        totalCost+=row['Cost']

    return totalCost    

#%%

production=[]
shoppingCart=[]
title=['Item', 'ProductName', 'Quantity', 'Price', 'Cost']

try:
    read_File('DataBase.csv', production)
except FileNotFoundError:
    print('File is not created...')
except IndexError:
    print('out of range...')


while True:
    choice_MainMenuOne=print_MainMenuOne()

    match choice_MainMenuOne:
        case 1:
            insert(production)
        case 2:
            system('clear')
            code = input('Please enter the desired code :')
            remove(production, search_CodeInProduction(code, production))
        case 3:
            system('clear')
            productName=input('Please enter the desired product name : ')
            edit(production, search_ProductNameInProduction(productName, production))
        case 4:
            while True:
                choice_MainMenuTwo=print_MainMenuTwo()

                match choice_MainMenuTwo:
                    case 1:
                        system('clear')
                        productName = input('Please enter the desired product name : ')
                        buy(production, shoppingCart, search_ProductNameInProduction(productName, production))
                    case 2:
                        print_PurchaseInvoice(len(shoppingCart)+1, len(title), shoppingCart, title, calculate_TotalCost(shoppingCart))
                        input()
                    case 3:
                        break
                    case _:
                        print_erorrs('Erorr! Your choice is false. Please try again...','red')
        case 5:
                try:
                    write_File('DataBase.csv', production)
                except FileNotFoundError:
                    print('File is not created...')
                except IndexError:
                    print('out of range...')  
                system('clear') 
                break
        case _:
            print_erorrs('Erorr! Your choice is false. Please try again...','red')