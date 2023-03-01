import unittest
from Boooooooooooooob import adder

class My_Test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(4,4), 8)

    def test_kwargs(self):
        self.assertEqual(adder(a=20, b=10), 30)

    def test_mix(self):
        self.assertEqual(adder(15, a=25), 40)

    def test_diff(self):
        x = 20
        y = 0
        self.assertEqual(adder(0, -8, y, a=x), 12)

    def test_wrong_datatypes(self):
        self.assertEqual(adder('8', 'abs', '20'), 28)


if __name__ == "__main__":
    unittest.main()

