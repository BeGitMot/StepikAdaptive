import collections

def val(c):
    suit = c[- 1]
    face = c[0 : - 1]
    return [suit, m[face]]

m = {
         '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
         '10':10,'J':11,'Q':12,'K':13,'A':14
    }

suits = {'C', 'D', 'H', 'S'}

res = ""

cards = set(input().split())
cards_val_face = {str(val(c)[1]) + val(c)[0] for c in cards}
cards_val = {str(val(c)[1]) for c in cards}
cards_suits = {str(val(c)[0]) for c in cards}

#количество значений
val_cnt = collections.Counter()
for v in [str(val(c)[1]) for c in cards]:
     val_cnt[v] += 1

#print (cards_val)

#Royal Flush
#Consists of the ace, king, queen, jack and ten of a suit.
#10C JC QC KC AC
for s in suits:
    if {'K'+s, 'Q'+s, 'A'+s, '10'+s, 'J'+s}.issubset(cards):
        res = 'Royal Flush'
        break;

#Straight Flush
#Five cards of the same suit in numerical order.
#6C 7C 8C 9C 10C
#9C 10C JC QC KC
#2C 3C 4C 5C 6C
#10C JC QC KC AC
if res == "":
    for s in suits:
        for i in range(9):
            if {str(14 - i - j) + s for j in range(5)} == cards_val_face:
                res = 'Straight Flush'
                break;

#Four of a Kind
#Four cards with the same value.
#9C 9D 9H 9S
#QC QD QH QS

if res == "":
    for v in range(2, 15):
        if {str(v) + s for s in list(suits)}.issubset(cards_val_face):
            res = 'Four of a Kind'
            break;

#Full House
#Three cards of the same value, with the remaining two cards forming a pair
#9C 9D 9H QS QH

if res == "" and len(cards_val) == 2:
    res = "Full House"

#Flush
#Hand contains five cards of the same suit.
#10C 9C 2C 5C 6C
if res == "" and len(cards_suits) == 1:
    res = "Flush"

#Straight
#Hand contains five cards with consecutive values.
#2H 3S 4S 5D 6S
#10H JS QS KC AS

if res == "":
    for v in range(2, 11):
        if {str(v + i) for i in range(5)} == cards_val:
            res = 'Straight'
            break;

#Three of a Kind
#Three of the cards in the hand have the same value
#9H 9S 9Q KH 6D

if res == "" and val_cnt.most_common(1)[0][1] == 3:
    res = 'Three of a Kind'

#Two Pairs
#The hand contains two different pairs
#9H 9S AQ AH 6D
if res == "" and val_cnt.most_common(2)[0][1] == 2 and val_cnt.most_common(2)[1][1] == 2:
    res = 'Two Pairs'

#Pair
#Two of the five cards in the hand have the same value.
#9H 9S AQ 7H 6D
if res == "" and val_cnt.most_common(1)[0][1] == 2:
    res = 'Pair'

#High Card
#Hands which do not fit any higher category are ranked by the value of their highest card
#6H 9S AQ 7D 2D

if res == "":
    res = 'High Card'

#print (cards)
print (res)

