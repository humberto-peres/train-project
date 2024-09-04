import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from train.restriction import Restriction
from train.exceptions import ConstraintViolationException
class TestRestriction(unittest.TestCase):

    def setUp(self):
        self.restriction = Restriction()

    def test_validate_movements_length(self):
        commands = ['1'] * 51
        with self.assertRaises(ConstraintViolationException):
            self.restriction.validateMovements(commands)

    def test_validate_movements_consecutive(self):
        commands = ['1'] * 21
        with self.assertRaises(ConstraintViolationException):
            self.restriction.validateMovements(commands)

if __name__ == '__main__':
    unittest.main()
