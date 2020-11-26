"""Lab 8 - Crimetime Tests
CPE 101
Section: 3 & 7
Name: Amy Ru
Cal Poly User: amru
"""

import unittest
from crimetime import *

class MyTest(unittest.TestCase):
    def test_create_crimes(self):
        # testing create_crimes
        lines = ['150019937\tVANDALISM\tCONSPIRACY\n',
        '150017931\tASSAULT\tCREDIT CARD, THEFT BY USE OF\n',
        '120554383\tROBBERY\tFALSE IMPRISONMENT\n']
        expected = [Crime(150019937, 'VANDALISM'), Crime(150017931, 'ASSAULT'), 
        Crime(150025837, 'ROBBERY')]
        self.assertEqual(create_crimes(lines), expected)

    def test_sort_crimes(self):
        # testing sort_crimes
        crimes = [Crime(1, 'VANDALISM'), Crime(2, 'ASSAULT'), 
        Crime(3, 'ROBBERY')]
        expected = [Crime(1, 'VANDALISM'), Crime(2, 'ASSAULT'), 
        Crime(3, 'ROBBERY')]
        self.assertEqual(sort_crimes(crimes), expected)

    def test_set_crimetime(self):
        # testing set_crimetime
        crime1 = Crime(150019937, 'VANDALISM')
        set_crimetime(crime1, 'Tuesday', 1, 17)
        crime2 = Crime(150017931, 'ASSAULT')
        crime2.day_of_week = 'Wednesday'
        crime2.month = 'February'
        crime2.hour = '5PM'
        crime3 = Crime(150025837, 'ROBBERY')
        crime3.day_of_week = 'Thursday'
        crime3.month = 'March'
        crime3.hour = '6PM'
        self.assertEqual(crime1, crime2)
        self.assertEqual(crime2, crime3)
        self.assertEqual(crime1, crime3)
        

    def test_update_crimes(self):
        # testing update_crimes
        crimes = [Crime(1, 'VANDALISM'), Crime(2, 'ASSAULT'), 
        Crime(3, 'ROBBERY')]
        lines = ['1 Tuesday 01/06/2015 16:53', '2 Wednesday \
        02/03/2015 17:06', '3 Thursday 03/08/2015 18:30']
        crime1 = Crime(1, 'VANDALISM')
        crime1.day_of_week = 'Tuesday'
        crime1.month = 'January'
        crime1.hour = '4PM'
        crime2 = Crime(1, 'ASSAULT')
        crime2.day_of_week = 'Wednesday'
        crime2.month = 'February'
        crime2.hour = '5PM'
        crime3 = Crime(1, 'ROBBERY')
        crime3.day_of_week = 'Thursday'
        crime3.month = 'March'
        crime3.hour = '6PM'
        self.assertEqual(crimes[0], crime1)
        self.assertEqual(crimes[1], crime2)
        self.assertEqual(crimes[2], crime3)

    def test_find_crime(self):
        # testing find_crime
        crimes = [Crime(1, 'VANDALISM'), Crime(2, 'ASSAULT'), 
        Crime(3, 'ROBBERY')]
        self.assertEqual(find_crime(crimes, 1), Crime(1, 'VANDALISM'))
        self.assertEqual(find_crime(crimes, 2), Crime(2, 'ASSAULT'))
        self.assertEqual(find_crime(crimes, 3), Crime(3, 'ROBBERY'))

if __name__ == "__main__":
    unittest.main()