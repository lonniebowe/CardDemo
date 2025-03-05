import random

class PlayingCard:
    """A playing card class"""
    
    SUITS = ("Hearts", "Diamonds", "Clubs", "Spades")
    RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError("Invalid rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid suit")
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __eq__(self, other):
        if not isinstance(other, PlayingCard):
            return False
        return self.rank == other.rank and self.suit == other.suit

class Deck:
    """A deck of 52 playing cards"""
    
    def __init__(self):
        self.cards = [PlayingCard(rank, suit) for suit in PlayingCard.SUITS for rank in PlayingCard.RANKS]
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw_card(self):
        if not self.cards:
            raise ValueError("No cards left in the deck")
        return self.cards.pop()

class Hand:
    """A hand of playing cards"""
    
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        if not isinstance(card, PlayingCard):
            raise ValueError("Only PlayingCard instances can be added")
        self.cards.append(card)
    
    def display_hand(self):
        return ", ".join(str(card) for card in self.cards)
    
    def card_count(self):
        return len(self.cards)
