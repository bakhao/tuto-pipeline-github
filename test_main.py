import unittest
from main import ZeroPointTemperatureCalculator

DATA = [20, 70, 50, 100]
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_calculate(self): #test calculator for pipeline
        calculator = ZeroPointTemperatureCalculator()
        result = calculator.calculate(DATA)
        self.assertEqual(result, 60)
        pass
if __name__ == '__main__':
    unittest.main()
