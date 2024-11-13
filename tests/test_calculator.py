import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

print("sys.path:", sys.path)

import unittest
from src.classes.calculator import calculateWoundRoll

class TestCalculator(unittest.TestCase):

    def test_calculateWoundRoll(self):
        self.assertEqual(calculateWoundRoll(4, 4), 4)

if __name__ == '__main__':
    unittest.main()

#Test cases from first version:
# no re roll yet
#print("4x Melta rifles into Ctan")
#calculateDamage(4, 9, 3, 11, 4)
#print("2x Multi-melta into Ctan")
#calculateDamage(4, 9, 4, 11, 4)