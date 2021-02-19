from wip_array import infix as infix

#returns the index and character of the FIRST discrapancy between short and long wips
#delta = (character, index)
def find_delta(shorter_wip, longer_wip):
    S = shorter_wip
    L = longer_wip
    #assume no differences
    delta = (None, None)
    #check each letter in L
    for i in range(0, len(L)-1):
        #if the letter at the same index of S does not match, that's our delta
        if L[i] != S[i]:
            #delta = (character, index)
            delta = (L[i], i)
            break #we only want the FIRST delta, as every letter after the first discrepancy will also be different
    #if no discrepancies were found by the end of S, then by exhaustion, we can assume that the delta must be at the end of S
    if delta == (None, None) and L != S:
        delta = (L[-1], len(S))

    return delta
            
