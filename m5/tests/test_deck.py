import unittest
from hw5.deck import Deck
from hw5.card import Card


class TestDeck(unittest.TestCase):

    def test_deck_str(self):
        deck = Deck()
        deck_string = str(deck)
        self.assertEqual(len(deck_string), 685, "Checking str(deck) works properly.\nSubmitted:"+str(deck_string))

    def test_deck_getter(self):
        deck = Deck()
        self.assertTrue(len(deck.get_cards()) == 52, "Checking deck.get_deck() works properly.\nSubmitted:"+str(deck.get_cards()))

    def test_deck_setter_single_card(self):
        deck = Deck()
        new_deck = [Card("Heart", 4)]
        deck.set_cards(new_deck)
        self.assertEqual(deck.get_cards(), new_deck, "Checking set_deck() works properly for setting a single card deck. \nExpected:"+str(new_deck)+"\nSubmitted:"+str(deck.get_cards()))

    def test_deck_setter_no_cards(self):
        deck = Deck()
        deck.set_cards([])
        self.assertEqual(deck.get_cards(), [], "Checking deck.set_deck() works properly when the deck is empty.\nExpected: deck.get_deck() == []")

    def test_correct_suits_and_values(self):
        deck = Deck()
        for card in deck.get_cards():
            self.assertTrue(card.get_suit() in ["Heart", "Club", "Spade", "Diamond"], "Checking Deck() works properly. A card "+str(card)+" is out of four suits.")
            self.assertTrue(card.get_value() in range(1, 14), "Checking Deck() works properly. A card "+str(card)+" is out of range(1,14)")

    def test_deck_no_duplicates(self):
        deck = Deck()
        cards = deck.get_cards()
        for card_num in range(1, 53):
            card = cards.pop()
            self.assertTrue(card not in deck.get_cards(), "\nChecking pop() method must remove the popped card from the deck.\nCard: " + str(card) + " should not be in deck: " + str(deck.get_cards()))

    def test_deck_deal_cards(self):
        deck = Deck()
        while len(deck.get_cards())>0:
            last_card = deck.get_cards()[-1]
            proper_output = last_card
            submitted_output = deck.deal_card()
            self.assertEqual(proper_output, submitted_output, "Checking deck.deal_card() method returns the last card in the deck.\nExpected:"+str(proper_output)+"\nSubmitted:"+str(submitted_output))

unittest.main()