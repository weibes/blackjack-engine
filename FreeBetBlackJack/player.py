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

    def setMoney(self, money) -> None:
        self.money = money

    def getMoney(self) -> int:
        return self.money

    def dealCard(self, card) -> None:
        self.hand.append(card)

    def isBust(self) -> bool:
        return self.getHandCount() > 21

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

    