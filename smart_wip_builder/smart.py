from example import find_example_words as find
from wip_array import build_wip_array as build

def get_smart_wip(min_length = 4, min_examples = 5):
    #keeps track of the 'smartest' wip found so far from this test_wip_array
    smart_wip = ""
    while len(smart_wip) == 0:
        test_wip_array = build()
        for wip in test_wip_array:
            examples = find(wip)
            #store (and return) wip with min length and number of example
            #replace with a longer valid wip from same test_wip_array, if found
            if len(wip) >= min_length and len(examples) >= min_examples and len(wip) > len(smart_wip):
                smart_wip = wip
    return smart_wip

