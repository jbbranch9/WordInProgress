from example import find_example_words as find
from wip_array import build_wip_array as build

def build_smart_wip_list(length = 1):
    smart_wips = []
    while len(smart_wips) < length:
        test_wip_array = build("")
        for wip in test_wip_array:
            examples = find(wip)
            if len(wip) > 4 and len(examples) > 5:
                smart_wips.append(wip)
                print(smart_wips)
    return smart_wips


print(build_smart_wip_list())
print("DONE")