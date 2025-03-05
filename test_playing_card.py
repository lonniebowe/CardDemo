import unittest
from playing_card import PlayingCard, Deck, Hand

class TestPlayingCard(unittest.TestCase):

    def test_valid_card(self):
        card = PlayingCard("A", "Hearts")
        self.assertEqual(str(card), "A of Hearts")

    def test_invalid_rank(self):
        with self.assertRaises(ValueError):
            PlayingCard("1", "Hearts")

    def test_invalid_suit(self):
        with self.assertRaises(ValueError):
            PlayingCard("A", "Stars")

    def test_card_equality(self):
        card1 = PlayingCard("10", "Diamonds")
        card2 = PlayingCard("10", "Diamonds")
        self.assertEqual(card1, card2)

    def test_card_inequality(self):
        card1 = PlayingCard("10", "Diamonds")
        card2 = PlayingCard("J", "Diamonds")
        self.assertNotEqual(card1, card2)

class TestDeck(unittest.TestCase):

    def test_deck_size(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_shuffle(self):
        deck1 = Deck()
        deck2 = Deck()
        deck1.shuffle()
        self.assertNotEqual(deck1.cards, deck2.cards)  # Shuffled deck should be different

    def test_draw_card(self):
        deck = Deck()
        initial_size = len(deck.cards)
        card = deck.draw_card()
        self.assertIsInstance(card, PlayingCard)
        self.assertEqual(len(deck.cards), initial_size - 1)

    def test_draw_from_empty_deck(self):
        deck = Deck()
        for _ in range(52):
            deck.draw_card()
        with self.assertRaises(ValueError):
            deck.draw_card()

class TestHand(unittest.TestCase):

    def test_add_card(self):
        hand = Hand()
        card = PlayingCard("Q", "Spades")
        hand.add_card(card)
        self.assertIn(card, hand.cards)

    def test_display_hand(self):
        hand = Hand()
        card1 = PlayingCard("J", "Clubs")
        card2 = PlayingCard("7", "Hearts")
        hand.add_card(card1)
        hand.add_card(card2)
        self.assertEqual(hand.display_hand(), ["J of Clubs", "7 of Hearts"])

    def test_number_of_cards(self):
        hand = Hand()
        self.assertEqual(hand.number_of_cards(), 0)
        hand.add_card(PlayingCard("5", "Diamonds"))
        self.assertEqual(hand.number_of_cards(), 1)

if __name__ == "__main__":
    unittest.main()
