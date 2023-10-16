import csv
from hand import Hand
class BlackJackPlayer:
    """BlackJackPlayer Object A Player can initialized
        with a particular strategy, either as a preconfigured strategy, or as a custom
        list of betting/playing procedures.

    Arguments:
    starting_money: The amount of money the player starts with.
    strategy_config: String name of various types of strategies that a player could use.
    
    Returns: Player() Object 
    """
    def __init__(self, starting_money=1000, strategy_config='basic_strategy'):
        self.money = starting_money
        self.hands = []
        self.decision_tree = self.load_config(strategy_config)

    """
    load_config loads a custom config file setup into a Player object. Uses intended data structure,
    located in /data/README.md
    
    Arguments:
    strategy_config: configuration string signifying the intended strategy.
            really just gives what sub folder to read.
    
    returns: dictionary, containing a decision tree to parse.
    """
    def load_config(self, strategy_config):
        config_path = '../data' + strategy_config
        decision_tree = {}

        with open(config_path + 'hard.csv') as f:
            csvreader = csv.reader(f, delimiter=',')
            decision_tree['hard'] = self.load_config_helper(csvreader)  
 
        with open(config_path + 'soft.csv') as f:
            csvreader = csv.reader(f, delimiter=',')
            decision_tree['soft'] = self.load_config_helper(csvreader)  
 
        with open(config_path + 'split.csv') as f:
            csvreader = csv.reader(f, delimiter=',')
            decision_tree['split'] = self.load_config_helper(csvreader)  
 
        with open(config_path + 'surrender.csv') as f:
            csvreader = csv.reader(f, delimiter=',')
            decision_tree['surrender'] = self.load_config_helper(csvreader)  
 
        return decision_tree


    def load_config_helper(self, csvreader) -> dict:
        # create hard decision tree
        # dims are: first dim is player card, second dim is dealer card
        # so itr through hard: if you have a 15, and dealer has an A, you do
        # hard[15][A]
        decisions = {}
        player_hands = csvreader[0][1:] # remove first element which should always be invalid
        for row in csvreader[1:]: # read thru the rows, excluding top row which is player hands
            dealer_card = row[0]
            row_decision = {}
            for i in range(1, len(row)):
                row_decision[player_hands[i]] = row[i]
            decisions[dealer_card] = row_decision
        return decisions

    # TODO Add to config
    def calculate_num_hands_play(self) -> int:
        return 1 
    
    # calculate all bets for all hands
    # TODO Add to config, curr just bet 10 every time.
    def calculate_bets(self) -> list[int]:
        bet_list = []
        for hand in self.hands:
            bet_list.append(10)
        return bet_list
    
    # get a hand to play. Returns CURRENT index of the hand (not guaranteed to be consistent)
    def add_hand(self, hand: Hand) -> idx:
        self.hands.append(hand)
        return len(self.hands) - 1
    
    # peek a specific hand, doesn't pop out of players hands
    def peek_hand(self, idx: int) -> Hand:
        return self.hands[idx]

    # pop a specific hand out of the player's current hands
    def pop_hand(self, idx: int) -> Hand:
        return self.hands.pop(idx)
    
    # clears all hands the player currently holds. Good for in between rounds
    def clear_hands(self):
        self.hands = []
    
    # set the amount of money the player currently has
    def set_money(self, money: int):
        self.money = money

    # get the amt of money the player has
    def get_money(self) -> int:
        return self.money
    
    # get the count of a certain hand the player has
    def get_hand_count(self, idx: int) -> int:
        curr_hand = self.hands[idx]
        return curr_hand.calculate_hand_value()

    # get the decision for a particular hand
    def get_hand_decision(self, idx: int) -> int:
        curr_hand = self.hands[idx]
        # check if surrender


    # TODO Add config, currently just giving false.
    # calculate insurance for all players hands
    def calculate_insurance(self) -> list[bool]:
        return ['false' for x in self.hands]
    