#!/usr/bin/env python3
import random

print('please enter the Dice you want to roll in the Format ndx,')
print('where n is the count of dices, and x is the number of possible values of the dice, e.g. 2d6')
diceRaw = input()
diceList = diceRaw.split("d")
diceFaces = int(diceList[1])
diceCount = int(diceList[0])
diceOut = 0
i = 0

while i < diceCount:
    diceResult: int = random.randint(1, diceFaces)
    diceOut: int = diceOut + diceResult
    i += 1

print(diceOut)
