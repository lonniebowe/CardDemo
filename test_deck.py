
import unittest
from deck import Deck
from playing_card import PlayingCard

class TestDeck(unittest.TestCase):

    def test_deck_initialization(self):
        deck = Deck()
        self.assertEqual(len(deck), 52)

    def test_deck_shuffle(self):
        deck1 = Deck()
        deck2 = Deck()
        deck2.shuffle()
        self.assertNotEqual([str(card) for card in deck1.cards], [str(card) for card in deck2.cards])

    def test_draw_card(self):
        deck = Deck()
        card = deck.draw()
        self.assertIsInstance(card, PlayingCard)
        self.assertEqual(len(deck), 51)

    def test_draw_from_empty_deck(self):
        deck = Deck()
        for _ in range(52):
            deck.draw()
        with self.assertRaises(ValueError):
            deck.draw()

if __name__ == "__main__":
    unittest.main()
