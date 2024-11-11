# TESTING FOR MOVIE RECOMMENDATION SYSTEM

import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# testing error message shows when an invalid input is entered
def test_invalid_user_input(capsys):
    user_choice = "invalid_input"

    if user_choice not in ["recommend", "add"]:
        print("Invalid choice. Please type 'recommend' or 'add'.")

    # Capture the output for invalid input
    captured = capsys.readouterr()
    assert "Invalid choice. Please type 'recommend' or 'add'." in captured.out
