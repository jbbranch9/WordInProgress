from wip_list import build_list as build

from lexicon import word_list as lex

#print(lex)

def find_example_word(wip):
    example = ""
    wip_len = len(wip)

    if wip in lex:
        example = wip
    else:
        for word in lex:

            print("++++\nWORD: ", word, "\n++++\n")
            #assume the word is a valid example for this wip, then look for counter-examples by:
                #1) checks that each letter is in the would-be example word
                #2) checks that any letters that appear BEFORE a given "letter" in the "wip" also appear AT LEAST ONCE before that same "letter" in the "word"
                #3) repeat #2, checking letters that appear AFTER a given "letter" in the "wip"
            valid = True
            for index in range(0, wip_len):
                letter = wip[index]
                pre = wip[:index]
                post = wip[index+1:]

                print("    ====")
                print("    wip: ", wip, "\n    pre: ", pre, "\n    letter: ", letter, "\n    post: ", post)
                print("    valid: ", valid)
                print("    ====")
               

                #if the letter isn't in the word at all, word is not valid example for this wip
                if letter not in word:
                    valid = False
                    break
                #if any other letters exist BEFORE this "letter"
                if len(pre) > 0:
                    for other_letter in pre:
                        #if the FIRST occurance of "other_letter" is not until AFTER "letter" in "word"
                        if word.find(other_letter) > index or other_letter not in word:
                            valid = False
                            break
                #if any other letters exist AFTER this "letter"
                if len(post) > 0:
                    for other_letter in post:
                        #if the LAST occurance of "other_letter" is BEFORE "letter" in "word"
                        if word.rfind(other_letter) < index or other_letter not in word:
                            valid = False
                            break

                print("        ----")
                print("        still_valid: ", valid)
                print("        ----")

                #if still valid at this point, then "word" is proven to be a valid example for "wip"
                if valid:
                    example = word
                else:
                    break

            #once example word is no longer empty string, we don't need to keep looping through "word"(s) in "lex"
            if example != "":
                break

    return example

(find_example_word("noth"))

