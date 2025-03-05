from playing_card import PlayingCard
import random

class Deck:
    """A deck of playing cards"""

    def __init__(self):
        self.cards = [PlayingCard(rank, suit) for suit in PlayingCard.SUITS for rank in PlayingCard.RANKS]
    
    def shuffle(self):
        """Shuffles the deck"""
        random.shuffle(self.cards)
    
    def draw(self):
        """Draws a card from the deck"""
        if not self.cards:
            raise ValueError("No cards left in the deck")
        return self.cards.pop()
    
    def __len__(self):
        """Returns the number of cards left in the deck"""
        return len(self.cards)

