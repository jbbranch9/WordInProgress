frequency = ['110', '19', '37', '57', '175', '29', '26', '81', '94', '1', '9', '53', '31', '90', '100', '25', '0', '80', '84', '122', '37', '12', '31', '1', '26', '0']
alphabet = "abcdefghijklmnopqrstuvwxyz"

def get_unweighted():
    return alphabet

def get_weighted():
    weighted = ""
    for i in range(26):
        weighted += alphabet[i]*int(frequency[i])
    return alphabet + weighted


new_list = []
for i in frequency:
    new_list.append(str(int(i)-1))

