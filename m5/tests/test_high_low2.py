import unittest
from hw5.player import *
from hw5.high_low import HighLow


class TestHighLow(unittest.TestCase):
    def test_deal_cards_many_players_full_deck(self):
        players = []
        for player_id in range(1, 53):
            players.append(Player(str(player_id)))
            game = HighLow(players)
            game.deal_cards()
            self.assertEqual(len(game.get_deck().get_cards()), 52 % len(players), "Remaining cards in the deck after deal_cards must be 52 % len(players). But "+str(len(game.get_deck().get_cards()))+" cards remain in your code.")

    def test_deal_cards_many_players_full_deck_game(self):
        players = []
        for player_id in range(1, 53):
            players.append(Player(str(player_id)))
            game = HighLow(players)
            winners = game.winners()
            for player in players:
                self.assertEqual(player.get_cards(), [])
                if player not in winners:
                    self.assertTrue(winners[0].get_points() > player.get_points(), "Testing game.winners() method. Winners' points must be bigger than any non-winner's points.")

    def test_deal_cards_many_players_full_deck_total_point_value_game(self):
        players = []
        for player_id in range(1, 53):
            total_points = 0
            players.append(Player(str(player_id)))
            for player in players:
                player.set_points(0)
            game = HighLow(players)
            game.play_game()
            winners = game.winners()
            for player in players:
                self.assertEqual(player.get_cards(), [], "After playing game, players don't have any card in hands.")
                total_points += player.get_points()
                if player not in winners:
                    self.assertTrue(winners[0].get_points() > player.get_points(), "Testing game.winners() method. Winners' points must be bigger than any non-winner's points.")
            self.assertEqual(total_points, 52/player_id, "The sum of points of all the players is 52.")


unittest.main()