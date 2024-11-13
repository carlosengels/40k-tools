import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Add the 'src' directory to sys.path
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Get the base directory
src_path = os.path.join(base_path, 'src')  # Path to the 'src' folder
sys.path.insert(0, src_path)  # Insert it at the start of sys.path

# Print the sys.path to confirm
print("sys.path:", sys.path)

import unittest
from src.classes.calculator import calculateWoundRoll

class TestCalculator(unittest.TestCase):

    def test_calculateWoundRoll(self):
        self.assertEqual(calculateWoundRoll(4, 4), 4)

if __name__ == '__main__':
    unittest.main()