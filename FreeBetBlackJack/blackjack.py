from . import deck

## Goal of this file: Create basic simulation system, ALlow for easy input into the systema

"""
what is needed for classes:
2. a Simulator
3. basic functional tests for above
4. a simulator script

"""


class BlackJack:

    def __init__(self, num_players=1, num_decks=8):
        self.deck = deck.Deck()
    
    def 