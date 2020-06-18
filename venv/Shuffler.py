from random import randint, shuffle
from array import array
import pdb
from time import sleep

# array uses less memory than the python 'list'
# def pause(multiply=1):
#     for i in list(range(100000*multiply)):
#         pass
# arr = array('i',[1,2,3,4,5])
# print (arr)
# R = range(1, players + 1)

pack_of_cards = ['2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Ah',
                 '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Ad',
                 '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 'Jc', 'Qc', 'Ac',
                 '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'As']

shuffled_deck = pack_of_cards

shuffle(shuffled_deck)

print(f'Shuffled deck: \n {shuffled_deck}')

players = input('How many players in this game? ')
players = int(players)

dealt = {}

for p in range(1,players+1):
    dealt[p]=[]

holecards = 2
cardcount = 0
print(dealt) #temp

class PlayerCards:
    def __init__(self, number_of_hole_cards):
        self.number_of_hole_cards = number_of_hole_cards

    def deal_hole_cards (self):
        for deal_round in range(1, self.number_of_hole_cards + 1):
            for player in dealt.keys():
                dealt[player].append(shuffled_deck[cardcount])
                cardcount += 1
        return (dealt)

    def add_card_to_players_hands (self, *cardlist): #list param
        for c in len(cardlist):
            for player in dealt.keys():
                dealt[player].append(cardlist[c])
        return (dealt)

Texas_holdem = PlayerCards(2)

print(Texas_holdem)
sleep(1)
print("Burn card ")#{shuffled_deck[cardcount]}")
sleep(1)
print("flop = \n-----")

flop = []
for cards in range(3):
    sleep(1)
    cardcount +=1
    flop.append(shuffled_deck[cardcount])
    print(shuffled_deck[cardcount])

print(add_card_to_players_hands(flop))

cardcount +=2
turn = shuffled_deck[cardcount]

print(add_card_to_players_hands(turn))

cardcount +=2
river = shuffled_deck[cardcount]

print(add_card_to_players_hands(river))

the_board = flop.copy()
the_board.append(turn)
the_board.append(river)
sleep(1)
print('burn and turn...')
sleep(2)
print(turn)
sleep(1)
print('burn card, river...')
sleep(2)
print(river)

print(the_board)
#print(flop)

sleep(3)


