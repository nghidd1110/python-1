import time
time.sleep(1)

import random

ranks=("2","3","4","5","6","7","8","9","10","J","Q","K","A")
suits=("hearts","diamonds","clubs","spades")
deck = [(rank,suit) for rank in ranks for suit in suits]

random.shuffle(deck)
p1_deck=deck[:27]
p2_deck=deck[27:]

def comparaison(p1_deck,p2_deck):
    if ranks.index(p1_deck[0]) == ranks.index(p2_deck[0]):
        return 0
    elif ranks.index(p1_deck[0]) > ranks.index(p2_deck[0]):
        return 1
    elif ranks.index(p1_deck[0]) < ranks.index(p2_deck[0]):
        return 2   

def gameloop(p1_deck,p2_deck):
    while len(p1_deck)>0 and len(p2_deck)>0:
        p1_card=p1_deck.pop(0)
        p2_card=p2_deck.pop(0)
        result = comparaison(p1_card,p2_card)
        if result==0:
            war(p1_deck, p2_deck, [p1_card,p2_card])
        elif result==1:
            p1_deck.append(p1_card)
            p1_deck.append(p2_card)
        elif result==2:
            p2_deck.append(p2_card)
            p2_deck.append(p1_card)
    if len(p1_deck)>0 and len(p2_deck)==0:
        print ("PLAYER 1 IS THE WINNER!")
    elif len(p1_deck)==0 and len(p2_deck)>0:
        print("PLAYER 2 IS THE WINNER!")
    elif len(p1_deck)==0 and len(p2_deck)==0:
        print("NO ONE WON!")

def war(p1_deck,p2_deck,winning_deck):
    if len(p1_deck)<4 or len(p2_deck)<4:
        if len(p1_deck) > len(p2_deck):
            p2_deck = []
        elif len(p1_deck) < len(p2_deck):
            p1_deck = []
        else:
            p1_deck = []
            p2_deck = []
        return
    winning_deck.extend(p1_deck.pop(0) for _ in range(3))
    winning_deck.extend(p2_deck.pop(0) for _ in range(3))
    card_1=p1_deck.pop(0)
    card_2=p2_deck.pop(0)
    winning_deck.append(card_1)
    winning_deck.append(card_2)
    result=comparaison(card_1,card_2)
    if result ==1:
        p1_deck.extend(winning_deck)
    elif result==2:
        p2_deck.extend(winning_deck)
    elif result ==0:
        war(p1_deck,p2_deck,winning_deck)    

gameloop(p1_deck,p2_deck)
