from .deck import Deck
from .player import Player
## Goal of this file: Create basic simulation system, ALlow for easy input into the systems

"""
what is needed for classes:
2. a Simulator
3. basic functional tests for above
4. a simulator script

"""

class BlackJack:

    # TODO: Add configs for diff tables - table configs, side bets, etc. 
    def __init__(self, num_players=1, num_decks=8, player_starting_bet=1000):
        self.deck = Deck(num_decks)
        self.player_list = [Player(player_starting_bet) for i in range(num_players)]

    def getPlayerList(self):
        return self.player_list

    def play_hand(self, players_list: list[Player]) -> list[bool]:
        dealer = Player(0)
        # collect player bets
        bets = [player.getBet() for player in players_list]
        # deal initial hands
        for i in range(2):
            for player in players_list:
                player.dealCard(self.deck.dealCard())
            dealer.dealCard(self.deck.dealCard())
        # check for BlackJack, offer insurance
        if dealer.getHand()[0] == 'A':  # first card in hand
            # offer insurance
            for player in players_list:
                if player.inHand() and player.wantInsurance():
                    
        # go thru each player
        
        # dealer plays game

        # wind down game. Give money out as needed, shuffle deck if needed according to deck pen, etc.