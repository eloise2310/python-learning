# TESTING USING PYTEST
# same example as in unittesting 

from phonebook import Phonebook
import pytest # so we can use pytest.raises

@pytest.fixture # adding the fixture so we dont have to put phonebook = Phonebook() in each test
def phonebook():
    phonebook = Phonebook()
    return phonebook

# checks looking up a name returns the correct number
def test_lookup_by_name(phonebook):
    # phonebook = Phonebook() --> would need this without the fixture - instead we can just add phonebook to the perameters
    phonebook.add("Eloise", "07730363008")
    number = phonebook.lookup("Eloise")
    assert number == "07730363008"

# checks all names can be looked up
def test_contains_all_names(phonebook):
    phonebook.add("Eloise", "07730363008")
    assert phonebook.all_names() == {"Eloise"}

# checks looking up a non existent name in the phonebook raises an error
def test_missing_name(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Eloise")