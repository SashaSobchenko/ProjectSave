import unittest
from bob import adder

class My_Test(unittest.TestCase):
    def test_args(self):
        assert adder(2, 2) == 4
        assert adder(a=5, b=10) == 15
        assert adder(10, a=20) == 30
        assert adder(0, -5, 0, a=10) == 5
        assert adder('5', 'abs', '10') == 15

if __name__ == "__main__":
    unittest.main()

