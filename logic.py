from random import choice
from copy import deepcopy
import os
import time

# removes an element from a list


def rem(list, phrase):
    for g in range(len(list)):
        list[g] = list[g].strip(phrase)
    return list


# Converts term to definition and definiton to term
def succ(vocab, label):
    ind = vocab.index(label)
    if ind % 2 == 0:
        return vocab[ind+1]
    else:
        return vocab[ind - 1]


with open('input.in', 'r') as full_elements:
    full_elements = full_elements.readlines()
full_elements = rem(full_elements, '\n')

# removes the spaces
while '' in full_elements:
    full_elements.remove('')
times = int(input('How many times should the set repeat?\n>'))
# Sets how many times you want to study the set
study_elements = times*full_elements
print(study_elements)
while study_elements:
    question = choice(study_elements)
    ans = succ(full_elements, question)
    print(question)
    ans_player = input('Enter answer\n>')
    # If the answer is correct
    if ans_player == ans:
        study_elements.remove(question)
        print('Correct!')
        input('press enter to continue')
        os.system('cls')
    # If the answer is wrong
    else:
        print('Inorrect...')
        print(f'The correct answer is {ans}')
        input('press enter to continue')
        os.system('cls')
