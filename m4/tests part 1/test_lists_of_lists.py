from hw4_part1.lists_of_lists import *
import unittest

time1 = [9,45,"AM"]
time2 = [12,4,"PM"]
time3 = [11,59, "PM"]
time4 = [12,1,"AM"]
time5 = [1,1,"AM"]
times = [time1, time2, time3]
str1 = "09:45 AM"
str2 = "12:04 PM"


class TestConditional(unittest.TestCase):

    def test_time_of_day1(self):
        result = time_of_day(times,0)
        self.assertEqual(result,str1)

    def test_time_of_day2(self):
        result = time_of_day(times,1)
        self.assertEqual(result,str2)

    def test_compare_time1(self):
        result = time_comparator(time1,time2)
        self.assertEqual(result,-1)

    def test_compare_time2(self):
        result = time_comparator(time2,time1)
        self.assertEqual(result,1)

    def test_compare_time3(self):
        result = time_comparator(time2,time3)
        self.assertEqual(result, -1)

    def test_compare_time4(self):
        result = time_comparator(time4,time5)
        self.assertEqual(result, -1)

    def test_latest_time1(self):
        result = latest_time(times)
        self.assertEqual(time3,result)

if __name__ == '__main__':
    unittest.main()
