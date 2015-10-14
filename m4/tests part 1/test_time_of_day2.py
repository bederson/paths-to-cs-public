from hw4_part1.lists_of_lists import *
import unittest

time1 = [9,45,"AM"]
time2 = [12,4,"PM"]
time3 = [11,59, "PM"]
time4 = [12,1,"AM"]
time5 = [1,1,"AM"]
times = [time1, time2, time3, time4, time5]
str1 = "09:45 AM"
str2 = "12:04 PM"

class TestConditional(unittest.TestCase):

    def test_time_of_day2(self):
        result = time_of_day(times,1)
        self.assertEqual(result,str2)


if __name__ == '__main__':
    unittest.main()
