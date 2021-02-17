from wip_list import build_list as build

from lexicon import word_list as lex

lex = set(lex)

def validate_example(wip, example):

    valid = False

    wip_len = len(wip)

    for index in range(0,wip_len):
        letter = wip[index]

        if letter in example:
            #if checking FIRST letter in "wip"
            if index == 0:
                last_verified_index = 0
                continue

            #if checking SECOND through LAST letter in "wip"
            else:
                if example.rfind(letter) <= last_verified_index:
                    valid = False
                    break
                else:
                    last_verified_index = index
                    valid = True
                    continue
        else:
            break

    

    return valid


print(validate_example("hnbd", "husband"))


def find_examples_list(wip):

    valid_example_list = []

    wip_len = len(wip)

    #check every word in lex for match
    for word in lex:
        #for each word, check each letter of the wip
        for index in range(0,wip_len):
            letter = wip[index]
            #if "letter" isn't in "word", break
            #otherwise find instance in "word"

            if letter in word:

                if index == 0:

                    last_verified_index = word.find(letter)

                else:
                    
                    if word.rfind(letter) < last_verified_index:
                        break

                    else:
                        pass
                
                last_verified_index = index



            else:
                break


    return valid_example_list



print("DONE")