import unittest

from src import board


class TestTodoMethods(unittest.TestCase):

    def test_filler_space(self):
        space = board.filler_space(100, 5, "Hello")
        self.assertEqual(len(space), 90)


if __name__ == "__main__":
    unittest.main()
