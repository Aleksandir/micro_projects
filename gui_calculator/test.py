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
        self.assertEqual(evaluate_calculation("2**3"), "8")  # Exponentiation
        self.assertEqual(evaluate_calculation("2*3**2"), "18")  # Order of operations
        self.assertEqual(
            evaluate_calculation("2*(3**2)"), "18"
        )  # Order of operations with parentheses
        self.assertEqual(
            evaluate_calculation("2*3**2+5"), "23"
        )  # Order of operations with addition
        self.assertEqual(
            evaluate_calculation("2*(3**2+5)"), "28"
        )  # Order of operations with parentheses and addition
        self.assertEqual(evaluate_calculation("2*"), "Error")  # Incomplete expression
        self.assertEqual(evaluate_calculation(""), "Error")  # Empty expression
        self.assertEqual(evaluate_calculation("2/0"), "Error")  # Division by zero


if __name__ == "__main__":
    unittest.main()
