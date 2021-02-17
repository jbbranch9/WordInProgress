from wip_list import build_list as build

from lexicon import word_list as lex

lex = set(lex)

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

                print("\n\n\n")
                print(word)
                print(wip)
                print(letter)


                #if this is the first "letter" we're checking for this "word",
                if index == 0:
                    #then store the index of the FIRST instance of this "letter" in this "word"
                    last_verified_index = word.find(letter)

                    print('first letter found: ', letter)

                else:
                    #if this "letter" IS in this "word", AND it is NOT the first letter of the "wip",
                    #AND we have reached the last letter of the WIP
                    #then check if the LAST instance of this "letter" in this "word" is AFTER the "last_verified_index" (i.e. has a larger index)
                    
                    print('next letter found: ', letter)
                    
                    if last_verified_index < word.rfind(letter):
                        print("in order")
                        if index == wip_len:
                            valid_example_list.append(word)
                        else:
                            print("out of order, break")
                            continue
                    else:
                        break



            else:
                break


    return valid_example_list

print(find_examples_list("hlo"))

print("DONE")