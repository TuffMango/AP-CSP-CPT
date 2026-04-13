deck = [
    "One of Hearts", "Two of Hearts", "Three of Hearts", "Four of Hearts", "Five of Hearts", 
    "Six of Hearts", "Seven of Hearts", "Eight of Hearts", "Nine of Hearts", "Ten of Hearts", 
    "Jack of Hearts", "Queen of Hearts", "King of Hearts",
    
    "One of Diamonds", "Two of Diamonds", "Three of Diamonds", "Four of Diamonds", "Five of Diamonds", 
    "Six of Diamonds", "Seven of Diamonds", "Eight of Diamonds", "Nine of Diamonds", "Ten of Diamonds", 
    "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds",
    
    "One of Clubs", "Two of Clubs", "Three of Clubs", "Four of Clubs", "Five of Clubs", 
    "Six of Clubs", "Seven of Clubs", "Eight of Clubs", "Nine of Clubs", "Ten of Clubs", 
    "Jack of Clubs", "Queen of Clubs", "King of Clubs",
    
    "One of Spades", "Two of Spades", "Three of Spades", "Four of Spades", "Five of Spades", 
    "Six of Spades", "Seven of Spades", "Eight of Spades", "Nine of Spades", "Ten of Spades", 
    "Jack of Spades", "Queen of Spades", "King of Spades"
]
import time
import math
import sys
import random

print("Welcome to Texas Hold em' Poker Simulator \n")       # beginning sequence
print("Dealing cards...\n")
time.sleep(2)

def playercards():                      #Me and Nathan Together, deals cards to user
    print("Your cards \n")
    playercard1 = random.choice(deck)
    deck.remove(playercard1)
    print(playercard1)
    playercard2 = random.choice(deck)
    print(playercard2)
    deck.remove(playercard2)
   


playercards()
def bot1():
    botcard1 = random.choice(deck)
    deck.remove(botcard1)
    botcard2 = random.choice(deck)
    deck.remove(botcard2)

bot1()

def first3():
    card1 = random.choice(deck)
    deck.remove(card1)
    card2 = random.choice(deck)
    deck.remove(card2)
    card3 = random.choice(deck)
    deck.remove(card3)
    print("\tCards on the table \n\t-----------------------")
    print(f"{card1}, {card2}, {card3}")
    

first3()
