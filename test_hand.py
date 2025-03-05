import unittest
from hand import Hand
from playing_card import PlayingCard

class TestHand(unittest.TestCase):

    def test_add_card(self):
        hand = Hand()
        card = PlayingCard("A", "Spades")
        hand.add_card(card)
        self.assertEqual(len(hand), 1)
        self.assertEqual(str(hand), "A of Spades")

    def test_remove_card(self):
        hand = Hand()
        card = PlayingCard("10", "Diamonds")
        hand.add_card(card)
        hand.remove_card(card)
        self.assertEqual(len(hand), 0)

    def test_remove_nonexistent_card(self):
        hand = Hand()
        card = PlayingCard("J", "Hearts")
        with self.assertRaises(ValueError):
            hand.remove_card(card)

    def test_add_invalid_card(self):
        hand = Hand()
        with self.assertRaises(ValueError):
            hand.add_card("Not a card")

if __name__ == "__main__":
    unittest.main()

