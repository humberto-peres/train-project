import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from train.movement import Movement
class TestMovement(unittest.TestCase):

    def setUp(self):
        self.movement = Movement()

    def test_move_left(self):
        self.assertEqual(self.movement.moveLeft(), -1)

    def test_move_right(self):
        self.assertEqual(self.movement.moveRight(), 1)

if __name__ == '__main__':
    unittest.main()
