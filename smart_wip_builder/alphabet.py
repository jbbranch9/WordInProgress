from random import randint

frequency = [110, 19, 37, 57, 175, 29, 26, 81, 94, 1, 9, 53, 31, 90, 100, 25, 0, 80, 84, 122, 37, 12, 31, 1, 26, 0]
unweighted = "abcdefghijklmnopqrstuvwxyz"

def get_unweighted():
    return unweighted


#default 'weight' is based on letter frequency in written English
def get_weighted(extra_weight = ""):
    for i in range(26):
        extra_weight += unweighted[i]*frequency[i]
    return unweighted + extra_weight

#use rand_letter_weighted and rand_letter_unweighted instead
def rand_letter(weighted_alphabet):
    index = randint(0, len(weighted_alphabet)-1)
    return weighted_alphabet[index]

def rand_letter_unweighted():
    return rand_letter(unweighted)

#"extra_weight" is a string of letters that should be more frequent/heavily weighted, 
#each instance of a letter in "extra_weight" is like adding extra 'tickets' for that letter to the hypothetical letter 'raffle'
def rand_letter_weighted(extra_weight = ""):
    return rand_letter(get_weighted(extra_weight))
