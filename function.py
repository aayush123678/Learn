from random import choice, randrange, shuffle
import os


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
        return vocab[ind-1]

# Written questions


def written(study_elements, full_elements):
    wrong_list = []
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
            wrong_list.append(question)
            print('Inorrect...')
            print(f'The correct answer is {ans}')
            while ans_player != ans:
                ans_player = input('type correct answer:')
            input('Correct!\nPress enter to continue')
            os.system('cls')
    print('You have completed the set')


def multiple_choice(study_elements, full_elements):
    wrong_list = []
    while study_elements:
        os.system('cls')
        question = choice(study_elements)

        if full_elements.index(question) % 2 == 0:
            mc1 = full_elements[randrange(0, len(full_elements), 2)]
            mc2 = full_elements[randrange(0, len(full_elements), 2)]
            mc3 = full_elements[randrange(0, len(full_elements), 2)]
        else:
            mc1 = full_elements[randrange(1, len(full_elements), 2)]
            mc2 = full_elements[randrange(1, len(full_elements), 2)]
            mc3 = full_elements[randrange(1, len(full_elements), 2)]
        ans = succ(full_elements, question)
        print(question)
        print('a', succ(full_elements, question))
        choices = [ans, mc1, mc2, mc3]
        shuffle(choices)
        print(question)
        for g in range(1, 5):
            print(f"{g}.{choices[g-1]}")
        ans_player = int(input('Enter answer\n>'))
        if choices[ans_player-1] == ans:
            print('Correct')
            study_elements.remove(question)
            input('Press enter to continue...')
        else:
            wrong_list.append(question)
            print('Inorrect...')
            print(f'The correct answer is {ans}')
            input('Press enter to continue...')
    print('You have completed this set')
