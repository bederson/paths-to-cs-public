import unittest
from random import randint
from hw5.card import *


class TestCard(unittest.TestCase):

    def test_card_str(self):
        for i in range(100):
            suit = ["Heart", "Spade", "Club", "Diamond"][randint(0, 3)]
            num = randint(1, 13)
            card = Card(suit, num)
            proper_output = "(" + suit + ", " + str(num) + ")"
            submission_output = str(card)
            self.assertEqual(proper_output, submission_output, "Check str(card) method works properly.\nExpected: "+proper_output+"\nSubmitted:"+submission_output)

    def test_card_getter(self):
        for i in range(100):
            suit = ["Heart", "Spade", "Club", "Diamond"][randint(0, 3)]
            num = randint(1, 13)
            card = Card(suit, num)
            self.assertEqual(card.get_suit(), suit, "Check card.get_suit() returns the correct suit.\nExpected: "+str(card.get_suit())+"\nSubmitted:"+str(suit))
            self.assertEqual(card.get_value(), num, "Check card.get_value() returns the correct value.\nExpected: "+str(card.get_value())+"\nSubmitted:"+str(num))


unittest.main()