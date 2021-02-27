from smart import get_smart_wip
from wip_array import build_wip_array as build_array_around
from difference import find_delta as delta
from example import find_example_words as examples

def game(min_wip_length = 7, min_word_examples = 3):

    wip = get_smart_wip(min_wip_length, min_word_examples)

    #print(wip)

    frames = build_array_around(wip)

    #print(frames)

    #pause = input()

    game_data = []
    for frame in frames:
        wip = frame
        
        frame_data = {}
        

        frame_data["wip"] = wip
        
        name = str(len(wip))

        if len(name) == 1:
            name = "0" + name
        frame_data["frame"] = str(name)

        frame_data["examples"] = examples(wip)

        game_data.append(frame_data)

    for i in range(0, len(game_data)-1):
        frame = game_data[i]
        next_frame = game_data[i+1]
        S = frame["wip"]
        L = next_frame["wip"]

        frame["delta"] = delta(S, L)
    
    game_data[-1]["delta"] = (None, None)


    return game_data

data = game()

for i in reversed(data):
    print(i)
print("DONE")