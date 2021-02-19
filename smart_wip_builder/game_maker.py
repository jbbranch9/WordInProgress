from smart import get_smart_wip
from wip_array import build_wip_array as build_array_around

def game():

    #wip = get_smart_wip(5, 7)
    wip = "hello"
    frames = build_array_around(wip)



    game_data = []
    for frame in frames:
        frame_data = {}
        frame_data["wip"] = frame
        frame_data

    return frames



print(game())
print("DONE")