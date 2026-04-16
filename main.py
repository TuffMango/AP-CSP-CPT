#fork test
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

print("Welcome to the BlackJack Simulator \n")       # beginning sequence
print("Dealing cards...\n")
time.sleep(2)

def playercards():                      #Me and Nathan Together, deals cards to user
    print("\nYour cards")
    playercard1 = random.choice(deck)
    deck.remove(playercard1)
    playercard2 = random.choice(deck)
    deck.remove(playercard2)
    print(f"You: {playercard1}, {playercard2}\n")


def bot1():
    botcard1 = random.choice(deck)
    deck.remove(botcard1)
    botcard2 = random.choice(deck)
    deck.remove(botcard2)
    print(f"Bot cards: {botcard1}, {botcard2}\n")

def dealer():
    dealercard1 = random.choice(deck)
    deck.remove(dealercard1)
    dealercard2hidden = random.choice(deck)
    deck.remove(dealercard2hidden)
    print(f"Dealer: {dealercard1}, Hidden")

dealer()
playercards()
bot1()


player_money = 500
pot = 0
player_bet = int(input("Please place your bet(max 500):  \n"))
while player_bet < 1 :
    player_bet = int(input("Please place your bet:  \n"))
pot = player_bet + pot
bot1_money = random.randint(1, 300)
print(f"Amount on table is {pot} \n")
time.sleep(2)
print(f"You have ${player_money} \n")
time.sleep(4)
print("Bot One's turn...")
time.sleep(3)
pot = pot + bot1_money
print(f"Bot 1 added {bot1_money}, current pot is now {pot} \n")
time.sleep(4)
print("Bot Two's turn...")
bot2_money = random.randint(1, 300)
pot = pot + bot2_money
print(f"Bot Two added {bot2_money}, current pot is now {pot} \n")



    
    

    






            

        
    


