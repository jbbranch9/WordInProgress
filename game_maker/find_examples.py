from validate import validate_example_word as validate
from lexicon import lexicon as lex
from wip_array import build_list as build_list




wip_list = build_list()

print("\n\n\n", wip_list[29], "\n\n\n")

for frame in wip_list:
    wip = frame["wip"]
    examples = []
    for example_word in lex:
        #print(example_word)
        if validate(wip, example_word):
            examples.append(example_word)

    frame["examples"] = examples

for frame in wip_list:
    print(frame)
    pause = input()
    