import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from train.train import Train
from train.exceptions import InvalidCommandException, ConstraintViolationException

class TestTrain(unittest.TestCase):

    def setUp(self):
        self.train = Train()

    def test_initial_position(self):
        self.assertEqual(self.train.position, 0)

    def test_execute_commands(self):
        commands = ['1', '2', '1']
        end_position, route = self.train.execute(commands)
        self.assertEqual(end_position, -1)
        self.assertEqual(route, [0, -1, 0, -1])

    def test_execute_commands_with_restriction(self):
        commands = ['1'] * 21
        with self.assertRaises(ConstraintViolationException):
            self.train.execute(commands)

    def test_invalid_command(self):
        commands = ['3']
        with self.assertRaises(InvalidCommandException):
            self.train.execute(commands)

if __name__ == '__main__':
    unittest.main()
