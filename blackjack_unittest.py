import unittest
import blackjack
import random

class blackjackTest(unittest.TestCase):

    def test_card_class(self):
        suit = random.choice(blackjack.suits)
        rank = random.choice(blackjack.ranks)
        value = blackjack.values[rank]

        card_result = blackjack.Card(suit, rank)
        print(card_result)

        self.assertEqual(card_result.suit, suit)
        self.assertEqual(card_result.rank, rank)
        self.assertEqual(card_result.value, value)


    def test_deck_class(self):
        create_deck = blackjack.Deck()
        print(create_deck)
        
        length_deck = len(create_deck.deck)
        first_card = str(create_deck.deck[0])
        last_card = str(create_deck.deck[-1])
        self.assertEqual(length_deck, 52)
        self.assertEqual(first_card, 'Two of Hearts')
        self.assertEqual(last_card, 'Ace of Clubs')

        first_deal = create_deck.deal()
        self.assertEqual(len(create_deck.deck), 51)

    def test_hand_class(self):
        suit = random.choice(blackjack.suits)
        rank = random.choice(blackjack.ranks)
        value = blackjack.values[rank]

        card_result = blackjack.Card(suit, rank)
        create_hand = blackjack.Hand()
        create_hand.add_card(card_result)
        print(create_hand.value)
        print(create_hand.aces)
        print(create_hand.cards[0])

    def test_chips_class(self):
        chips = blackjack.Chips()
        
        #Total Check
        chips.total = int(input("Please enter your total amount of chips: "))
        self.assertEqual(chips.total, 100)
       
        #Win Check
        chips.bet = 10
        chips.win_bet()
        self.assertEqual(chips.total, 110)

        #Lose Check
        chips.bet = 20
        chips.lose_bet()
        self.assertEqual(chips.total, 90)


if __name__ == '__main__':
    unittest.main()
