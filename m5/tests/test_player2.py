import unittest
from hw5.card import *
from hw5.player import *


class TestPlayer(unittest.TestCase):
    def test_player_play_cards(self):
        cards = []
        player = Player("Alfred")
        for suit in ["Heart", "Club", "Spade", "Diamond", "dodecahedron"]:
            for value in range(1, 100):
                card = Card(suit, value)
                cards.append(card)
                player.add_card(card)
        while player.has_cards():
            self.assertEqual(player.play_card(), cards.pop(), "Testing play_card() returning the last card in the player's hand.")


unittest.main()
