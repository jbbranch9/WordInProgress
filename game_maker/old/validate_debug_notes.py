def validate_example(wip, example):
    last_verified_index = None

    valid = True

    for index in range(0,len(wip)):
        letter = wip[index]

        if letter in example:
            #if checking FIRST letter in "wip"
            if index == 0:
                #then "last_verified_index" is first/leftmost instance of "letter" in "example"
                last_verified_index = example.find(letter)

            #if checking SECOND through LAST letter in "wip"
            else:
                #substring of everthing in "example" after "last_verified_index"
                after_last_verified = example[last_verified_index+1:]

                #if an instance of "letter" exists in "example" 
                if letter in after_last_verified:
                    #the new "last_verified_index" is defined as: the FIRST instance of "letter" in "after_last_verified"
                    #i.e. the index within "after_last_verified" plus the length of the example up to that point
                    last_verified_index = after_last_verified.find(letter) + len(example[:last_verified_index+1])

                else:
                    valid = False

        else:
            valid = False

    return valid