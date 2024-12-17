import random

print("Welcome to the solo adventure, Slitherin escapees!\nHow would you like to proceed?")
print("1. Play\n2. Options\n3. Quit")
int(input("")) == menuopt

if menuopt == "1":
    

player_health = 100


print("You wake up in a dark cell, you can't make out where you are but you see a door with a dimm light. You get 2 options, inspect the cell or inspect the door.")

cellopt = int(input("1 or 2"))

if cellopt == 1:
    print("In the cell you notice a loose toilet and a bed with a compartement under it, would you like to inspect the toilet or under the bed? Put: Toilet or Bed.")

elif cellopt == 2:
    print("You inspect the door and shout for help to see if anyone is out there, but instead you are met with a fierce human head that throws you off-guard. You hurridly pull yourself back as a man with a human face on him is already with haste walking towards you. He lifts you up with immense strength and bashes your head into the stone cold wall. You have fallen, Game over!")
