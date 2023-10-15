
"""
class Hand holds basic calculations related to a blackjack hand. Able to calculate a hand's value, and determine if the hand is bust, soft, splittable. To be used by a Player and a Game.

"""
class Hand():

    def __init__(self, cards: list[str]):
        self.cards = cards
        self.calculate_hand_value()
    
    def get_cards(self) -> list[str]:
        return self.cards
    
    def add_card(self, card: str):
        self.cards.append(card)
    
    def calculate_hand_value(self) -> int:
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
        self.set_is_bust(count)
        self.set_is_soft(aces_count)
        return count
    
    def get_is_bust(self) -> bool:
        return self.bust
    
    def set_is_bust(self, count: int):
        self.bust =  count >= 22

    def get_is_soft(self) -> bool:
        return self.soft

    def set_is_soft(self, aces_count: int):
        self.soft = aces_count >= 1
    
    def calculate_can_split(self) -> bool:
        return len(self.cards) == 2 and self.cards[0] == self.cards[1]
