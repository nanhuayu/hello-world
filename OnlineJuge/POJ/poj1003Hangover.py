
hang = [0]
card = [0]

def hang_card(hang,card):
    hang_len = len(hang)
    #print hang
    #print hang_len
    if hang[-1] <= card:
        while hang[-1] < card:
            hang.append(1000000/(hang_len + 1) + hang[-1] + 1)
            hang_len += 1
        return hang_len - 1
    else:
        for i in range(hang_len):
            if hang[i] >= card:
                return i

def getline(card):
    try:
        card[0] = int(float(raw_input())*1000000)
        return True
    except EOFError:
        return False

while getline(card):
    if card[0] == 0:
        continue
    #print card[0]
    print hang_card(hang, card[0]), "card(s)"