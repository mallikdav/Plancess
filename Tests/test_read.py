__author__ = 'Mallik'
import unittest
from userStory1 import read

class TestReadEntries(unittest.TestCase):

    def test_read_zeroes(self):
        input = " _  _  _  _  _  _  _  _  _ "\
                "| || || || || || || || || |"\
                "|_||_||_||_||_||_||_||_||_|"

        account_number = read.parse_account_number(input)
        self.assert_(account_number == '000000000')

    def test_read_ones(self):
        input = "                           "\
                "  |  |  |  |  |  |  |  |  |"\
                "  |  |  |  |  |  |  |  |  |"

        account_number = read.parse_account_number(input)
        self.assert_(account_number == '111111111')

    def test_get_account_numbers_from_file(self):
        filename = 'scan.txt'
        account_numbers = read.get_account_numbers_from_file(filename)
        self.assert_(account_numbers[10] == '123456789')

if __name__ == '__main__':
    unittest.main()