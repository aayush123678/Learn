from random import choice, randrange, shuffle
import os

from function import rem, succ, written,multiple_choice


# extracts the file information
with open('test.in', 'r') as full_elements:
    full_elements = full_elements.readlines()
full_elements = rem(full_elements, '\n')
print(full_elements)
# removes the extra spaces in the file
while '' in full_elements:
    full_elements.remove('')
print(full_elements)
evens = full_elements[::2]
odds = full_elements[1::2]
while len(odds) < 4:
    odds.append(None)
while len(evens) < 4:
    evens.append(None)
# Multiple choice or written?
#questions_type = input('Mutiple choice or written? m/w\n>')
questions_type = 'm'
# Sets how many times you want to study the set
#times = int(input('How many times should the set repeat?\n>'))
times = 1
study_elements = times*full_elements
os.system('cls')
if questions_type.lower() == 'w':
    written(study_elements, full_elements)
elif questions_type.lower() == 'm':
    multiple_choice(study_elements, full_elements, evens, odds)

