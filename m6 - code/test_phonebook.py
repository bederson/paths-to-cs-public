import unittest
from phonebook import *

class TestPhonebook(unittest.TestCase):
    def setUp(self):
        self.pb = Phonebook()

    def testAddOne(self):
        self.pb.add("Ben", "1234")
        self.assertIn("Ben", self.pb.getNames())
        self.assertIn("1234", self.pb.get("Ben"))

    def testAddSeveral(self):
        self.pb.add("Ben", "1234")
        self.pb.add("Ben", "5678")
        self.assertIn("Ben", self.pb.getNames())
        self.assertIn("1234", self.pb.get("Ben"))

unittest.main()