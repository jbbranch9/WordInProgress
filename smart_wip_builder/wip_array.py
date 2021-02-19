from alphabet import rand_letter_weighted as get_letter
from random import randint

#inserts "letter" into "wip" @ "index"
def infix(wip, letter, index):
    #if out of range, just append letter to end of wip
    if index > len(wip):
        wip = wip + letter
    else:
        wip = wip[:index] + letter + wip[index:]
    return wip

#used to reverse-engineer a wip from a "seed" back down to a single character 
#(build_wip_array can only ADD letters. this ensures the array is a full 30 frames)
def deconstruct(seed):
    deconstructions = [seed]
    while len(seed) > 1:
        index = randint(0, len(seed)-1)
        seed = seed[:index] + seed[index+1:]
        deconstructions.append(seed)
    return deconstructions

#generates the 30-frame evolutionary pattern of a wip
#can be seeded with a 'starter frame', which will occur at some point in the array
#otherwise each character, from and including the first, is random
def build_wip_array(seed = ""):
    if len(seed) == 0:
        wip = get_letter()
        wip_list = []
    else:
        wip = seed
        wip_list = deconstruct(seed)

    wip_list.append(wip)

    while len(wip) < 30:

        wip = infix(wip, get_letter(), randint(0, len(wip)-1))

        wip_list.append(wip)
    

    wip_list = set(wip_list)
    wip_list = list(wip_list)#
    wip_list = sorted(wip_list, key=len)


    return wip_list

#print(build_wip_array("hello"))

