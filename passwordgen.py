#!/usr/bin/env python3
import string
import random
print('Erstellt ein sicheres und leicht zu merkendes Passwort')
#loads all the languages words, numbers and special characters into lists
words = [line.rstrip('\n') for line in open("deutsch.txt")]
numbers = [1,2,3,4,5,6,7,8,9,0]
special = ["!", "§", "$", "%", "&", "=", "?", "+", "#", "-","*"]

#chooses 3 random words
part0 = random.choice(words)
part1 = random.choice(words)
part2 = random.choice(words)

#chooses the supplicants (1 number, 1 special char and determines their position)
if random.randint(0, 1) == 0:
    supp0 = str(random.choice(numbers))
    supp1 = random.choice(special)
else:
    supp0 = random.choice(special)
    supp1 = str(random.choice(numbers))

#assembling everything into one string and printing
password = part0 + supp0 + part1 + supp1 + part2
print(password)
