from os import path
import sys
import unittest
sys.path.append(path.abspath('../FreeBetBlackJack'))
from deck import Deck, STARTING_LIST

    """TODO:
    Tests for errors when written in future
    """

class TestDeck(unittest.TestCase):

    def test_initialization(self):
        deck = Deck()
        self.assertEqual(deck.num_decks, 8)
        self.assertEqual(deck.numCardsLeft(), 8 * len(STARTING_LIST))

    def test_dealCard(self):
        deck = Deck()
        card = deck.dealCard()
        self.assertIn(card, STARTING_LIST)
        self.assertEqual(deck.numCardsLeft(), 8 * len(STARTING_LIST) - 1)

    def test_numCardsLeft(self):
        deck = Deck(num_decks=2)
        self.assertEqual(deck.numCardsLeft(), 2 * len(STARTING_LIST))
        deck.dealCard()
        self.assertEqual(deck.numCardsLeft(), 2 * len(STARTING_LIST) - 1)

    def test_shuffleDeck(self):
        deck1 = Deck(num_decks=1)
        deck2 = Deck(num_decks=1)
        # Assuming that two shuffles won't result in the same order.
        # (not a perfect test, but it should work most of the time)
        self.assertNotEqual(deck1.deck, deck2.deck)

if __name__ == "__main__":
    unittest.main()
