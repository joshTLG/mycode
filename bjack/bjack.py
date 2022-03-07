#!/usr/bin/python3
import random

dealer_cards = []

player_cards = []

while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print(f"Dealer has: {dealer_cards[1]}")

while len(player_cards) != 2:
    player_cards.append(random.randint(1,11))
    if len(player_cards) ==2:
        print(f"Player has: {player_cards}")

if sum(dealer_cards) == 21:
    print("Dealer has 21 and wins")
elif sum(dealer_cards) > 21:
    print("Dealer busts")

while sum(player_cards) < 21:
    action = str(input("Stay or Hit?" ))
    if action == "hit":
        player_cards.append(random.randint(1, 11))
        print("Player has " + str(sum(player_cards)))
    else:
        print("Dealer has " + str(sum(dealer_cards)))
        print("PLayer has " + str(sum(player_cards)))
        if sum(dealer_cards) > sum(player_cards):
            print("Dealer wins")
        else:
            print(

