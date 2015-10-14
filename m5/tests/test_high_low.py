import unittest
from hw5.card import *
from hw5.player import *
from hw5.deck import Deck
from hw5.high_low import HighLow


class TestHighLow(unittest.TestCase):

    def test_high_low_one_player_str(self):
        ted = Player("Ted")
        players = [ted]
        submitted_output = HighLow(players)
        proper_output = "Ted, Points: 0, Cards Left: 0\n"
        self.assertEqual(proper_output, str(submitted_output), "The test runs HighLow() with a single player 'Ted'. \nExpected:"+proper_output+"\nSubmitted:"+str(submitted_output))

    def test_high_low_two_players_str(self):
        ted = Player("Ted")
        bob = Player("Bob")
        players = [ted, bob]
        submitted_output= HighLow(players)
        proper_output = "Ted, Points: 0, Cards Left: 0\nBob, Points: 0, Cards Left: 0\n"
        self.assertEqual(proper_output, str(submitted_output), "The test runs HighLow() with two players Ted and Bob. \nExpected:"+proper_output+"\nSubmitted:"+str(submitted_output))

    def test_high_low_four_players_str(self):
        ted = Player("Ted")
        bob = Player("Bob")
        fred = Player("Fred")
        clancy = Player("Clancy")
        players = [ted, bob, fred, clancy]
        submitted_output = HighLow(players)
        proper_output = "Ted, Points: 0, Cards Left: 0\nBob, Points: 0, Cards Left: 0\nFred, Points: 0, Cards Left: 0\nClancy, Points: 0, Cards Left: 0\n"
        self.assertEqual(proper_output, str(submitted_output), "The test runs HighLow() with four players.\nExpected:"+proper_output+"\nSubmitted:"+str(submitted_output))

    def test_high_low_get_player(self):
        ted = Player("Ted")
        players = [ted]
        first_game = HighLow(players)
        self.assertEqual(players, first_game.get_players(), "Checks whether get_players() method works correctly.\nExpected:"+str([])+"\nSubmitted:"+str(first_game.get_players()))
        second_game = HighLow([])
        self.assertEqual([], second_game.get_players(), "Checks whether get_players() method works correctly..\nExpected:"+str([])+"\nSubmitted:"+str(second_game.get_players()))

    def test_high_low_set_players(self):
        ted = Player("Ted")
        bob = Player("Bob")
        fred = Player("Fred")
        clancy = Player("Clancy")
        game = HighLow([ted, bob])
        game.set_players([fred, clancy])
        proper_output = "Fred, Points: 0, Cards Left: 0\nClancy, Points: 0, Cards Left: 0\n"
        self.assertEqual(proper_output, str(game), "Checks whether set_players() method correctly replaces prior players in the game.\nExpected:"+proper_output+"\nSubmitted:"+str(game))

    def test_high_low_get_and_set_deck(self):
        ted = Player("Ted")
        bob = Player("Bob")
        game = HighLow([ted, bob])
        deck = Deck()
        deck.set_cards([Card("Heart", 4)])
        game.set_deck(deck)
        self.assertEqual(game.get_deck(), deck, "Checks set_deck() method replaces the prior deck.\nExpected:"+str(deck)+"\nSubmitted:"+str(game.get_deck()))

    def test_deal_cards_one_player_one_card(self):
        player = Player("Joe")
        card = Card("Hearts", 4)
        game = HighLow([player])
        game.get_deck().set_cards([card])
        game.deal_cards()
        self.assertEqual(len(game.get_deck().get_cards()), 0, "Checks whether deal_cards() method works correctly.\nExpected: empty deck after dealing the deck with a card \nSubmitted:"+str(game.get_deck().get_cards()))
        self.assertEqual(player.play_card(), card, "Checks whether deal() and play_card() method works correctly for a deck with a single card.")

    def test_deal_cards_two_players_two_cards(self):
        bruce = Player("Bruce")
        clark = Player("Clark")
        two_of_hearts = Card("Heart", 2)
        three_of_hearts = Card("Heart", 3)
        deck = Deck()
        deck.set_cards([two_of_hearts, three_of_hearts])
        game = HighLow([bruce, clark])
        game.set_deck(deck)
        game.deal_cards()
        self.assertEqual(len(game.get_deck().get_cards()), 0, "Starting with two cards in the deck, after dealing them to two players, there should be no cards in the deck.\nSubmitted:"+str(game.get_deck().get_cards()))
        self.assertEqual(bruce.play_card(), three_of_hearts, "Make sure game.deal_cards() gives the correct card to the player, and play_card() returns the card.")
        self.assertEqual(clark.play_card(), two_of_hearts, "Make suregame.deal_cards() gives the correct card to the player, and play_card() returns the card.")

    def test_deal_cards_four_players_full_deck(self):
        bruce = Player("Bruce")
        clark = Player("Clark")
        game = HighLow([bruce, clark])
        game.deal_cards()
        self.assertEqual(len(game.get_deck().get_cards()), 0, "Runs deal_cars() method with an empty deck. After being dealt, the deck should be empty.\nSubmitted:"+str(game.get_deck().get_cards()))

    def test_high_low_two_players_two_card_round(self):
        bruce = Player("Bruce")
        clark = Player("Clark")
        two_of_hearts = Card("Heart", 2)
        three_of_hearts = Card("Heart", 3)
        deck = Deck()
        deck.set_cards([two_of_hearts, three_of_hearts])
        game = HighLow([bruce, clark])
        game.set_deck(deck)
        game.deal_cards()
        game.play_round()
        self.assertFalse(bruce.has_cards(), "After playing a round with one card, there should be no card remaining in the player's hand.\nSubmitted:"+str(bruce.get_cards()))
        self.assertFalse(clark.has_cards(), "After playing a round with one card, there should be no card remaining in the player's hand.\nSubmitted:"+str(clark.get_cards()))
        self.assertEqual(bruce.get_points(), 1, "Checking the result of game with 'Heart-2' and 'Heart-3' cards. The player with 'Heart-3' wins 1 point.\nSubmitted:"+str(bruce.get_points()))
        self.assertEqual(clark.get_points(), 0, "Checking the result of game with 'Heart-2' and 'Heart-3' cards. The player with 'Heart-2' wins 0 point.\nSubmitted:"+str(clark.get_points()))

    def test_high_low_two_players_two_cards_same_value_round(self):
        bruce = Player("Bruce")
        clark = Player("Clark")
        two_of_hearts = Card("Heart", 2)
        three_of_hearts = Card("Spade", 2)
        deck = Deck()
        deck.set_cards([two_of_hearts, three_of_hearts])
        game = HighLow([bruce, clark])
        game.set_deck(deck)
        game.deal_cards()
        game.play_round()
        self.assertFalse(bruce.has_cards(), "After playing a round with one card, there should be no card remaining.\nSubmitted:"+str(bruce.get_cards()))
        self.assertFalse(clark.has_cards(), "After playing a round with one card, there should be no card remaining.\nSubmitted:"+str(clark.get_cards()))
        self.assertEqual(bruce.get_points(), 1, "Checking the result of game with 'Heart-2' and 'Spade-2' cards. The player with 'Heart-2' wins 1 point.\nSubmitted:"+str(bruce.get_points()))
        self.assertEqual(clark.get_points(), 0, "Checking the result of game with 'Heart-2' and 'Spade-2' cards. The player with 'Spade-2' wins 0 point.\nSubmitted:"+str(clark.get_points()))

    def test_high_low_three_players_four_card_round(self):
        bruce = Player("Bruce")
        clark = Player("Clark")
        lex = Player("Lex")
        two_of_hearts = Card("Heart", 2)
        three_of_hearts = Card("Heart", 3)
        four_of_hearts = Card("Heart", 4)
        five_of_hearts = Card("Heart", 5)
        deck = Deck()
        deck.set_cards([two_of_hearts, three_of_hearts, four_of_hearts, five_of_hearts])
        game = HighLow([bruce, clark, lex])
        game.set_deck(deck)
        game.deal_cards()
        game.play_round()
        self.assertEqual(len(game.get_deck().get_cards()), 1, "With four cards in the deck, after dealing to three players, one card should remain in the deck.")
        self.assertFalse(bruce.has_cards(), "After playing a round with one card, there should be no card remaining.")
        self.assertFalse(clark.has_cards(), "After playing a round with one card, there should be no card remaining.")
        self.assertFalse(lex.has_cards(), "After playing a round with one card, there should be no card remaining.")
        self.assertEqual(bruce.get_points(), 1, "Testing game result.")
        self.assertEqual(clark.get_points(), 0, "Testing game result.")
        self.assertEqual(lex.get_points(), 0, "Testing game result.")

    def test_high_low_four_players_full_deck_round(self):
        bruce = Player("Bruce")
        clark = Player("Clark")
        lex = Player("Lex")
        jack = Player("Jack")
        players = [bruce, clark, lex, jack]
        game = HighLow(players)
        game.deal_cards()
        game.play_round()
        self.assertEqual(len(game.get_deck().get_cards()), 0, "After dealing standard deck to four players, no card should remain in the deck.")
        for player in players:
            self.assertEqual(len(player.get_cards()), 12, "Each players has 12 cards in their hands after being dealt.")

    def test_one_winner(self):
        clark = Player("Clark")
        lex = Player("Lex")
        game = HighLow([clark, lex])
        clark.set_points(1)
        self.assertEqual([clark], game.winners(), "Simple test for game.winners() method, which must return the player with the highest points so far.")

    def test_two_winner(self):
        clark = Player("Clark")
        lex = Player("Lex")
        game = HighLow([clark, lex])
        clark.set_points(1)
        lex.set_points(1)
        self.assertEqual([clark, lex], game.winners(), "Testing game.winners() method with two players having same points.")

    def test_high_low_two_players_two_card_game(self):
        bruce = Player("Bruce")
        clark = Player("Clark")
        two_of_hearts = Card("Heart", 2)
        two_of_spades = Card("Spade", 2)
        game = HighLow([bruce, clark])
        game.get_deck().set_cards([])
        bruce.set_cards([two_of_hearts])
        clark.set_cards([two_of_spades])
        game.play_game()
        self.assertEqual([clark], game.winners(), "Testing game.winners() method in complex setting.")

    def test_high_low_four_players_eight_cards_game(self):
        bruce = Player("Bruce")
        clark = Player("Clark")
        jack = Player("Jack")
        lex = Player("Lex")
        ace_of_hearts = Card("Heart", 1)
        two_of_hearts = Card("Heart", 2)
        three_of_hearts = Card("Heart", 3)
        four_of_hearts = Card("Heart", 4)
        five_of_hearts = Card("Heart", 5)
        six_of_hearts = Card("Heart", 6)
        seven_of_hearts = Card("Heart", 7)
        eight_of_hearts = Card("Heart", 8)
        game = HighLow([bruce, clark, lex, jack])
        jack.set_cards([ace_of_hearts, two_of_hearts])
        lex.set_cards([three_of_hearts, four_of_hearts])
        clark.set_cards([five_of_hearts, six_of_hearts])
        bruce.set_cards([seven_of_hearts, eight_of_hearts])
        game.get_deck().set_cards([])
        game.play_game()
        self.assertEqual([bruce], game.winners(), "Testing game.winners() method in complex setting..")

    def test_high_low_four_players_full_deck_game(self):
        bruce = Player("Bruce")
        clark = Player("Clark")
        jack = Player("Jack")
        lex = Player("Lex")
        players = [bruce, clark, lex, jack]
        game = HighLow(players)
        game.play_game()
        winners = game.winners()
        for player in players:
            self.assertEqual(player.get_cards(), [])
            if player not in winners:
                self.assertTrue(winners[0].get_points() > player.get_points(), "Testing game.winners() method in complex setting.")


unittest.main()