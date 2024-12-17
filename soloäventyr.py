import random

#Start
print("Welcome to the solo adventure, Slitherin escapees!\nHow would you like to proceed?")

print("1. Play\n2. Options\n3. Quit")

menuopt = int(input())

#Start Menu
if menuopt == 1:

    print(menu2)

elif menuopt == 2:

    print(options)

elif menuopt == 3:
    
    quit()

#Game Menu
def game_extract():
    return "1. New Game\n2. Continue\n. Tutorial"

menu2 = print(game_extract())

#Options
def options_def():
    return "1. Sound\n2. Text size\n3. Gore"

options = print(options_def())