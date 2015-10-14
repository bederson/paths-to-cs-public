import unittest
from hw5.card import *
from hw5.player import *


class TestPlayer(unittest.TestCase):

    def test_player_str(self):
        player = Player("Thomas")
        self.assertEqual(str(player), "Thomas, Points: 0")

    def test_player_getter_basic(self):
        player = Player("Bruce")
        self.assertEqual(player.get_name(), "Bruce")
        self.assertEqual(player.get_points(), 0)
        self.assertEqual(player.get_cards(), [])

    def test_player_setter(self):
        player = Player("James")
        player.set_points(42)
        self.assertEqual(player.get_points(), 42)
        card = Card("Heart", 4)
        player.set_cards([card])
        self.assertEqual(player.get_cards(), [card])

    def test_player_add_card_and_getter(self):
        player = Player("Dick")
        card = Card("Heart", 4)
        player.add_card(card)
        self.assertEqual(player.get_cards(), [card])

    def test_player_add_card(self):
        player = Player("Jason")
        cards = []
        for suit in ["Heart", "Club", "Spade", "Diamond"]:
            for value in range(1, 14):
                card = Card(suit, value)
                if card not in cards:
                    cards.append(card)
                    player.add_card(card)
                self.assertEqual(player.get_cards(), cards)

    def test_player_has_no_cards(self):
        player = Player("Tim")
        self.assertFalse(player.has_cards(), "Testing has_cards() with a newly created player having no card in his hand.")

    def test_player_has_a_card(self):
        player = Player("Carrie")
        card = Card("Heart", 4)
        player.add_card(card)
        self.assertTrue(player.has_cards(),  "Testing has_cards() with a player having one card in his hand.")

    def test_player_has_cards(self):
        player = Player("Stephanie")
        for suit in ["Heart", "Club", "Spade", "Diamond"]:
            for value in range(1, 14):
                card = Card(suit, value)
                player.add_card(card)
                self.assertTrue(player.has_cards(),  "Testing has_cards() with a player having cards in his hand.")

    def test_player_play_no_cards(self):
        player = Player("Damian")
        self.assertIsNone(player.play_card(), "Testing play_card() method when there's no card in the player's hand.")

    def test_player_play_a_card(self):
        player = Player("Barbra")
        card = Card("Heart", 4)
        player.add_card(card)
        new_card = player.play_card()
        self.assertEqual(card, new_card, "Testing play_card() returning the last card added by add_card() method.")


unittest.main()