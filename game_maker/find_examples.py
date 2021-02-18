from validate import validate_example_word as validate
from lexicon import lexicon as lex
from wip_array import build_list as build_list






def find_examples(wip_list):
    #"frame" is the keyed collection (dictionary) of all info for each 'frame' (letter addition) of the wip as it is built
    for frame in wip_list:
        wip = frame["wip"]
        examples = []
        for example_word in lex:
            if validate(wip, example_word):
                examples.append(example_word)

        frame["examples"] = examples

test_list = build_list()

for frame in test_list:
    print(frame)


find_examples(test_list)

print("\n\n\n")

for frame in test_list:
    print(frame)

