"""
Deck class - this class very basically controls a deck of cards or a shoe of cards. This allows you to do a few basic operations.
Deal a card
Tell you how many cards are left in the deck
Shuffle the deck
"""
from random import shuffle
STARTING_LIST = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Deck:

    def __init__(self, num_decks=8):
        self.num_decks = num_decks
        self.shuffleDeck()

    def shuffleDeck(self):
        self.deck = STARTING_LIST * self.num_decks
        shuffle(self.deck)

    def dealCard(self) -> str:
        return self.deck.pop()

    def numCardsLeft(self) -> int:
        return len(self.deck)
