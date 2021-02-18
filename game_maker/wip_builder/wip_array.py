from random import randint

#returns a random English letter
def rand_letter():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = randint(0, 25)
    return alphabet[index]

#returns a WEIGHTED random English letter
def wrand_letter():
    #'heavy' letters occur more often
    weighted_alphabet = "AAABBCCDDEEEEEEFFGGHHHIIIJKLLMMNNOOOPPQRRSSSSTTUVWXYZ"
    index = randint(0, len)
    return weighted_alphabet[index]

#builds a list 
def build_list():
       
    #wip is short for word_in_progress
    wip = rand_letter()

    wip_data = {"wip": wip,
            "last_insert": wip,
            "last_index": 0,
            }
    wip_list = [wip_data] 



    #iterate until longer than longest word in lexicon (30 letters, including the first one, added above)
    for infix in range(0,29):
        #store length of wip
        wip_len = len(wip)

        new_letter = rand_letter()
        new_index = randint(0, wip_len)



        #prefix scenario
        if new_index == 0:
            wip = new_letter + wip
        #suffix scenario
        elif new_index == wip_len:
            wip = wip + new_letter
        #infix scenario
        else:
            beginning = wip[:new_index]
            middle = new_letter
            end = wip[new_index:]

            wip = beginning + middle + end
        

        wip_data = {"wip": wip,
            "last_insert": new_letter,
            "last_index": new_index,
            }   
        wip_list.append(wip_data)


      

    return wip_list
