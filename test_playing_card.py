import unittest
from playing_card import Deck, PlayingCard, Hand

class TestDeck(unittest.TestCase):
    
    def test_deck_initialization(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
    
    def test_shuffle(self):
        deck = Deck()
        original_order = deck.cards[:]
        deck.shuffle()
        self.assertNotEqual(deck.cards, original_order)
    
    def test_draw_card(self):
        deck = Deck()
        card = deck.draw_card()
        self.assertIsInstance(card, PlayingCard)
        self.assertEqual(len(deck.cards), 51)
    
    def test_draw_from_empty_deck(self):
        deck = Deck()
        for _ in range(52):
            deck.draw_card()
        with self.assertRaises(ValueError):
            deck.draw_card()

class TestHand(unittest.TestCase):
    
    def test_add_card(self):
        hand = Hand()
        card = PlayingCard("A", "Hearts")
        hand.add_card(card)
        self.assertEqual(len(hand.cards), 1)
    
    def test_display_hand(self):
        hand = Hand()
        card1 = PlayingCard("A", "Hearts")
        card2 = PlayingCard("10", "Clubs")
        hand.add_card(card1)
        hand.add_card(card2)
        self.assertEqual(hand.display_hand(), "A of Hearts, 10 of Clubs")
    
    def test_card_count(self):
        hand = Hand()
        self.assertEqual(hand.card_count(), 0)
        hand.add_card(PlayingCard("K", "Diamonds"))
        self.assertEqual(hand.card_count(), 1)

if __name__ == "__main__":
    unittest.main()
