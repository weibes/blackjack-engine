import configparser
"""Player Object simply wraps a player into an object. A Player can initialized with a particular strategy, either as a preconfigured strategy, or as a custom list of betting/playing procedures.
"""
class Player:
    """Player Object

    Arguments:
    starting_money: The amount of money the player starts with.

    Returns: Player() Object 

    """

    def __init__(self, starting_money=1000, strategyConfig='basic_strategy'):
        config = configparser.ConfigParser()
        self.money = starting_money
        self.hand = []
        self.inHand = True

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
        return "St"
    
    # TODO: Implement with strategy
    def wantInsurance(self) -> bool:
        return False
    
    # TODO betting strategy
    def getBet(self) -> int:
        bet = 10
        self.setMoney(self.getMoney() - bet)
        return bet

    