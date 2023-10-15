import csv
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
        self.hand = []
        self.inHand = True
        self.loadConfig(strategy_config)

    def loadConfig(self, strategy_config):
        config_path = '../data' + strategy_config
        self.decision = {}
        self.hard = {}
        with open(config_path + 'hard.csv') as f:
            csvreader = csv.reader(f, delimiter=',')
            player_hand = csvreader[0]
            for row in csvreader[1:]:
                dealer_card = row[0]
                row_decision = {}
                for i in range(1, len(row[1:])):
                    curr_decision = row[i]
                for curr_decision in row[1]:
                    # setup into dict
                    row_decision[]
                    

    def setMoney(self, money: int) -> None:
        self.money = money

    def getMoney(self) -> int:
        return self.money

    def dealCard(self, card: str) -> None:
        self.hand.append(card)
    
    def getHand(self) -> list[str]:
        return self.hand
    
    def resetHand(self) -> None:
        self.hand = []

    def isBust(self) -> bool:
        return self.getHandCount() > 21

    def setInHand(self, inHand: bool) -> None:
        self.inHand = inHand
    
    def getInHand(self) -> bool:
        return self.inHand

    def getHandCount(self) -> int:
        count = 0
        aces_count = 0
        for card in self.hand:
            if card == "A":
                count += 11
                aces_count += 1
            else:
                count += int(card)
            while aces_count and count > 21:
                aces_count -= 1
                count -= 10
        return count

    # TODO: Implement actual logic of player hand
    def playHand(self, dealer_card: str, curr_value: int, isSoft: bool, isPair: bool) -> str:
        return "St
    
    # TODO: Implement with strategy
    def wantInsurance(self) -> bool:
        return False
    
    # TODO betting strategy
    def getBet(self) -> int:
        bet = 10
        self.setMoney(self.getMoney() - bet)
        return bet

    