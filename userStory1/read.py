__author__ = 'Mallik'
'''
User Story 1
  You work for a bank, which has recently purchased an ingenious machine to assist in reading letters and faxes sent in
  by branch offices. The machine scans the paper documents, and produces a file with a number of entries which each look
  like this:
    _  _     _  _  _  _  _
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|

Each entry is 4 lines long, and each line has 27 characters. The first 3 lines of each entry contain an account number
written using pipes and underscores, and the fourth line is blank. Each account number should have 9 digits, all of
which should be in the range 0-9. A normal file contains around 500 entries.

Your first task is to write a program that can take this file and parse it into actual account numbers.
'''

from userStory2.validate import validate_account
from userStory3.results import output

# number pattern each being 3x3 cells
CELL_VALUES = {
        ' _ | ||_|': 0,
        '     |  |': 1,
        ' _  _||_ ': 2,
        ' _  _| _|': 3,
        '   |_|  |': 4,
        ' _ |_  _|': 5,
        ' _ |_ |_|': 6,
        ' _   |  |': 7,
        ' _ |_||_|': 8,
        ' _ |_| _|': 9
}

def parse_account_number(input):
    # input has 9 3x3 "cells".
    # break it up into individual cells.
    cells = []

    # copy into lines
    lines = ["","",""]
    offset = 0

    for char in input:
        lines[offset] += char
        if len(lines[offset]) == 27:
            offset += 1

    for offset in range(0, 26, 3):
        # offset, 0 will be top left of cell
        # offset + 2, 2 will be bottom right
        cell = lines[0][offset:offset+3]
        cell += lines[1][offset:offset+3]
        cell += lines[2][offset:offset+3]

        cells.append(cell)
    cell_values = []
    for cell in cells:
        cell_values.append(CELL_VALUES.get(cell, -1))
    return ''.join(map(str, cell_values))

@output #for userStory3
@validate_account #for userStory2
def get_account_numbers_from_file(filename):
    """Returns all account numbers found in <filename>, as a list of str"""

    account_numbers = []

    linecount = 0
    numberlines = ''
    with open(filename, 'r') as f:
        for line in f:
            linecount += 1

            if (linecount % 4) == 0:
                account_numbers.append(parse_account_number(numberlines))
                numberlines = ''
            else:
                # make sure to trim trailing newline
                numberlines += line.rstrip('\n')

    return account_numbers