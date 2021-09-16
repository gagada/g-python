#Gerard Agada, 2021-08-25
#Blackjack Game

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
            

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.deck.append(created_card)
    
    def __str__(self):
        return str([str(item) for item in self.deck])

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        if card.rank == 'Ace':
            self.aces +=1
        self.value = self.value + card.value
              
    def adjust_for_ace(self):
        if self.aces > 0 and self.value != 21:
            self.value = self.value - 10
            self.aces -= 1

class Chips:
    
    def __init__(self):
        self.total = int(input("Please enter your total amount of chips: "))
        self.bet = 0
        
    def win_bet(self):
        self.total = self.bet + self.total
        
    
    def lose_bet(self):
        self.total = self.total - self.bet

def take_bet(chips):
    try:
        bet = int(input("Please place your bet using an integer: "))
        if bet > chips.total:
            raise ValueError("Sorry, you dont't have enough chips to bet that amount!")
    except ValueError:
        bet = int(input("Try again-Please place a bet that will cover the total amount of chips: "))
    except:
        print("Looks like you did not enter an integer!")
        bet = int(input("Try again-Please place your bet using an integer: "))
    else:
        print(f"You bet {bet}!")
        chips.bet = bet

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    return(hand)

def hit_or_stand(deck,hand):
    playing = True
    choice = 'CHOICE'
    while choice not in ['h','s']:
        choice = input("Please enter (h) to HIT or enter (s) to STAND: ")
        if choice == 'h':
            hit(deck,hand)
            return(playing)
        elif choice == 's':
            playing = False
            return(playing)
        else:
            print("Wrong input, please try again!")



def show_some(player,dealer):
    print("\n")
    print("Dealer has: ")
    print(dealer.cards[1])
    print("Player has: ")
    for card in player.cards:
        print(card)
    
def show_all(player,dealer):
    print("\n")
    print("Dealer has: ")
    for card in dealer.cards:
        print(card)
    print("Player has: ")
    for card in player.cards:
        print(card)

def player_busts(hand,chips):
    print(f" {hand.value} -- Player 1 has BUST!")
    for card in hand.cards:
        print(card)
    print("Dealer Wins!")
    chips.lose_bet()

def player_wins(hand,chips):
    print(f" {hand.value} -- Player 1 is the Winner!")
    for card in hand.cards:
        print(card)    
    chips.win_bet()

def dealer_busts(hand,chips):
    print(f" {hand.value} -- Dealer has BUST!")
    for card in hand.cards:
        print(card)
    print("Player Wins!")
    chips.win_bet()
    
def dealer_wins(hand,chips):
    print(f" {hand.value} -- The Dealer is the Winner!")
    for card in hand.cards:
        print(card)
    chips.lose_bet()

def push(hand,chips):
    print(f"{hand.value} -- PUSH!")
    chips.bet = 0
        
def main():

    playing = True

    while True:
        # Print an opening statement
        print("Welcome to Blackjack!\n")

        # Create & shuffle the deck, deal two cards to each player
        blackjack_deck = Deck()
        blackjack_deck.shuffle()
        
        player_one = Hand()
        dealer = Hand()

        player_one.add_card(blackjack_deck.deal())
        dealer.add_card(blackjack_deck.deal())
        player_one.add_card(blackjack_deck.deal())
        dealer.add_card(blackjack_deck.deal())        
        
        # Set up the Player's chips
        player_one_chips = Chips()

        # Prompt the Player for their bet
        take_bet(player_one_chips)

        # Show cards (but keep one dealer card hidden)
        show_some(player_one, dealer)

        while playing:
            # Prompt for Player to Hit or Stand
            playing = hit_or_stand(blackjack_deck, player_one)
            # Show cards (but keep one dealer card hidden)
            show_some(player_one, dealer)
            #If player's hand exceeds 21, run player_busts() and break out of loop.
            if player_one.value > 21:
                player_busts(player_one, player_one_chips)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_one.value <= 21:
            while dealer.value < 17:
                # Show all cards
                show_all(player_one, dealer)
                hit(blackjack_deck, dealer)
            # Different winning scenarios
            if dealer.value > 21:
                dealer_busts(dealer, player_one_chips)
            elif player_one.value > dealer.value:
                player_wins(player_one, player_one_chips)
            elif dealer.value > player_one.value:
                dealer_wins(dealer, player_one_chips)
            else:
                push(dealer, player_one_chips)
                print(f"{player_one.value} -- PUSH!")

        # Inform Player of their chips total
        print(f"Player 1 has {player_one_chips.total}.")
        choice = ' '
        while choice not in ['Y', 'N']:
            choice = input("Would you like to play Blackjack again? (Y) or (N)")
            if choice not in ['Y', 'N']:
                print("Sorry, invalid choice! Please select Y or N")
        if choice == 'Y':
            pass
        else:
            break

if __name__ == '__main__':
    main()