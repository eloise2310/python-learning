# UNIT TESTING 
# unit testing practice for a phonebook scenario 
# 'python3 -m unittest' in terminal to run test

import unittest # import the test
from phonebook import Phonebook # import phonebook class

# declare class containing tests
class PhoneBookTest(unittest.TestCase):

    # this set up fixture method allows us to call Phonebook using self.phonebook 
    def setUp(self) -> None:
        self.phonebook = Phonebook() 

    # tear down fixture method releases the resources 
    def tearDown(self) -> None:
        pass

    # first test case
    def test_lookup_by_name(self): # testing to look up someone in the phonebook by name 
        # phonebook = Phonebook() # calling the Phonebook class (would have to do this if we didnt include the set up fixture)
        self.phonebook.add("Eloise", "07730363008")
        number = self.phonebook.lookup("Eloise")

        self.assertEqual(number, "07730363008")

    # second test case
    def test_missing_name(self): # testing if the name is missing and if it is throws an error
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    # third test case etc
    # @unittest.skip("Work in progress") # can add this to skip the test
    def test_empty_phonebook_is_consistent(self):
        is_consistent = self.phonebook.is_consistent()
        self.assertTrue(is_consistent)

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add("Eloise", "07730363008")
        self.phonebook.add("Bob", "07978786005")
        self.assertTrue(self.phonebook.is_consistent())


    def test_is_consistent_with_duplicate_entries(self):
        self.phonebook.add("Eloise", "07730363008")
        self.phonebook.add("Sue", "07730363008") # same phone number as another person
        self.assertFalse(self.phonebook.is_consistent())