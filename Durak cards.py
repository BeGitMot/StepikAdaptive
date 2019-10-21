c1, c2 = input().split()
s = input()

#c1, c2 = "AH","AS"
#s = "D"

def getSuitAndValue(c):
    suit = c[- 1]
    face = c[0 : - 1]
    return [suit, m[face] * (100 if suit == s else 1)]

m = {'6' : 0, '7' : 1, '8' : 2, '9' : 3, '10' : 4, 'J' : 5, 'Q' : 6, 'K': 7, 'A' : 8}

if c1[0 : - 1] not in m.keys() or c2[0 : - 1] not in m.keys():
    print ("Error")
else:
    c1 = getSuitAndValue(c1)
    c2 = getSuitAndValue(c2)

    if (s in [c1[0], c2[0]] or c1[0] == c2[0]) and (c1 != c2)\
        and c1[0] in ['C', 'D', 'H', 'S']\
        and c2[0] in ['C', 'D', 'H', 'S']:
        print ("First" if c1[1] > c2[1] else "Second")
    else:
        print ("Error")
