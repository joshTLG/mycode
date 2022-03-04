#!/usr/bin/env python3



amount = int(input("Give me a number between 1 and 9001: " ))

if amount > 100:
    if amount > 500 and amount < 9000:
        print("You're probabaly Piccolo")
    else:
        if amount < 500 and amount > 400:
            print("You're probably Krillin")
        elif amount < 500 and amount > 300:
            print("It's just Yamcha")
        elif amount > 9000:
            print("IT'S OVER 9000!!!! IT'S GOKU")
        else:
            print("Nobody worth fighting, probably Yajirobi")
elif amount == 100:
    print("You're baby Gohan")
else:
    print("It's Bulma, I guess")
