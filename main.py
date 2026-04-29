#fork test

#play 21


import random

player_money = 500
bot_money = 500

#makes deck
def make_deck():
    deck = []
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    nums = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    for suit in suits:
        for num in nums:
            deck.append((num, suit))
    return deck

#finds the total for each player based on their cards
def calculate_total(cards):
    total = 0
    aces = 0

    for card in cards:  
        value = card[0]
        if value == "A":  
            total += 11
            aces += 1
        elif value in ["J", "Q", "K"]:
            total += 10
        else:
            total += int(value)

    while total > 21 and aces > 0:  
        total -= 10
        aces -= 1

    return total



def deal_card(deck, hand):
    card = random.choice(deck)
    deck.remove(card)
    hand.append(card)


def playgame():
    global player_money, bot_money

    deck = make_deck()
    player = []
    bot = []
    dealer = []
#bet
    while True:
        try:
            bet = int(input(f"Enter bet (Max {player_money}): "))
            if 1 <= bet <= player_money:
                break
            else:
                print("Please enter a valid bet")
        except:
            print("Enter a number.")

    pot = bet
    player_money -= bet

    bot_bet = random.randint(1, 300)
    pot += bot_bet

    print(f"Pot is {pot}")

    for i in range(2):
        deal_card(deck, player)
        deal_card(deck, bot)
        deal_card(deck, dealer)

    print(f"Your cards: {player}")
    print(f"Botcards: {bot}")
    print(f"Dealer shows: {dealer[0]}")

    while True:
        total = calculate_total(player)
        print(f"Your total: {total}")

        if total > 21:
            print("You bust!")
            return
	
        choice = input("Hit or Stand? ").lower()
        if choice == "hit":
            deal_card(deck, player)
            print(f"Your cards: {player}")
        else:
            break


    while calculate_total(bot) < 17:
        deal_card(deck, bot)

    while calculate_total(dealer) < 17:
        deal_card(deck, dealer)

    player_total = calculate_total(player)
    bot_total = calculate_total(bot)
    dealer_total = calculate_total(dealer)

    print(f"\nFinal Totals:")
    print(f"You: {player_total}")
    print(f"Bot: {bot_total}")
    print(f"Dealer: {dealer_total}")
#win conditions
    if player_total > 21:
        print("You lose.")
        bot_money += pot

    elif bot_total > 21 and dealer_total > 21:
        print("You win!")
        player_money += pot * 2

    elif player_total > bot_total and player_total > dealer_total:
        print("You win!")
        player_money += pot * 2

    else:
        print("You lose.")
        bot_money += pot


print("Welcome to Blackjack\n")
#potentially the end/loop
while player_money > 0:
    playgame()
    again = input("Play again? (y/n): ").lower()
    if again != "y":
        break

print("Game over")

