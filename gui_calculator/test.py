import unittest

from calc import evaluate_calculation


class TestCalculation(unittest.TestCase):
    def test_evaluate_calculation(self):
        self.assertEqual(evaluate_calculation("2*(3+5)"), "16")
        self.assertEqual(evaluate_calculation("2*3+5"), "11")
        self.assertEqual(
            evaluate_calculation("2*(3+5"), "Error"
        )  # Missing closing parenthesis
        self.assertEqual(
            evaluate_calculation("2*3+)5("), "Error"
        )  # Mismatched parentheses


if __name__ == "__main__":
    unittest.main()
