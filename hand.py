from playing_card import PlayingCard

class Hand:
    """A hand of playing cards"""

    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        """Adds a card to the hand"""
        if not isinstance(card, PlayingCard):
            raise ValueError("Can only add PlayingCard instances")
        self.cards.append(card)
    
    def remove_card(self, card):
        """Removes a card from the hand"""
        if card in self.cards:
            self.cards.remove(card)
        else:
            raise ValueError("Card not in hand")

    def __len__(self):
        """Returns the number of cards in hand"""
        return len(self.cards)

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)

