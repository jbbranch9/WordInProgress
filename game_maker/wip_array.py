from random import randint

#returns a WEIGHTED random English letter
#"extra_weight" is a string of letters that should be more probable, 
#it functions as if it were adding extra 'tickets' for certain letters to the 'letter raffle'
def wrand_letter(extra_weight = ""):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    #'heavy' letters occur more often
    weighted_alphabet = alphabet + extra_weight
    index = randint(0, len(weighted_alphabet)-1)
    return weighted_alphabet[index]


#builds a list 
def build_list():
       
    #wip is short for word_in_progress
    wip = wrand_letter()

    wip_data = {"wip": wip,
            "last_insert": wip,
            "last_index": 0,
            }
    wip_list = [wip_data] 



    #iterate until longer than longest word in lexicon (30 letters, including the first one, added above)
    for infix in range(0,29):
        #store length of wip
        wip_len = len(wip)

        new_letter = wrand_letter()
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
