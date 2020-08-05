import unittest

from functions import get_formatted_name

# It is customary to start method name with 'test_' in unittest model 
class NamesTestCase(unittest.TestCase):
    """ Tests for get_formatted_name function """

    def test_first_last_name(self):
        """ Do name like 'charlie chaplen' work """
        formatted_name = get_formatted_name('charlie', 'chaplen')
        self.assertEqual(formatted_name, 'Charlie Chaplen')

    def test_first_last_middle_name(self):
        """ Do names like 'Abdul Haseeb Bhutta' works """
        formatted_name = get_formatted_name('abdul', 'bhutta', 'haseeb')
        self.assertEqual(formatted_name, 'Abdul Haseeb Bhutta')

unittest.main()

"""
print("Enter 'q' to exit any time")

while True:
    first=input("Enter your first name:\t")
    if first=='q':
        break
    last=input("Enter your last name:\t")
    if last=='q':
        break

    name=get_formatted_name(first, last)
    print("Neatly formatted name is", name, ".")


"""
