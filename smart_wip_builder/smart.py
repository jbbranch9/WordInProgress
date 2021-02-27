from example import find_example_words as find
from wip_array import build_wip_array as build

def get_smart_wip(min_length = 3, min_examples = 2, seed_wip = ""):

    test_wip_array = build(seed_wip)

    shortlist = []
    for wip in test_wip_array:
        examples = find(wip)
        #add all frames of a wip array which meet "min_length" and "min_examples" criteria to the "shortlist"
        if len(wip) >= min_length and len(examples) >= min_examples:
            shortlist.append(wip)

    #print(shortlist)

    #find and return the longest wip from the shortlist
    smartest = ""
    for smart_wip in shortlist:
        if len(smart_wip) > len(smartest):
            smartest = smart_wip

    return smartest



print(get_smart_wip(7,2))
print("DONE")