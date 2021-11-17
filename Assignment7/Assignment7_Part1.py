from random import choice
from os import system
from termcolor import colored

boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']
results = []

for i in range(len(boys)):

    temp_boy= choice(boys)
    temp_girl= choice(girls)

    boys.remove(temp_boy)
    girls.remove(temp_girl)

    results.append((temp_boy, temp_girl))

system('clear')

for i in range(len(results)):
    print('{}- '.format(i+1)+colored(results[i][0], 'blue')+ ' is married to '+colored(results[i][1], 'red')+'\n')

input()

system('clear')