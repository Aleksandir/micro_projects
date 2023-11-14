import unittest

from weight_converter_dropdown import convert


class TestConvert(unittest.TestCase):
    def test_kg_to_lb(self):
        conversion_info = ("Kg to Lb", 2.20462)
        self.assertEqual(convert(1, conversion_info), 2.2046)
        self.assertEqual(convert(10, conversion_info), 22.0462)
        self.assertEqual(convert(100, conversion_info), 220.462)
        self.assertEqual(convert(1000, conversion_info), 2204.62)
        self.assertEqual(convert(-2, conversion_info), -4.40924)
        self.assertEqual(convert(-20, conversion_info), -44.0924)
        self.assertEqual(convert(-200, conversion_info), -440.924)
        self.assertEqual(convert(-2000, conversion_info), -4409.24)
        self.assertEqual(convert(0, conversion_info), 0)
        self.assertEqual(convert(0.5, conversion_info), 1.10231)
        self.assertEqual(convert(0.05, conversion_info), 0.11023)
        self.assertEqual(convert(0.005, conversion_info), 0.01102)

    def test_lb_to_kg(self):
        conversion_info = ("Lb to Kg", 0.453592)
        self.assertEqual(convert(1, conversion_info), 0.45359)
        self.assertEqual(convert(10, conversion_info), 4.53592)
        self.assertEqual(convert(100, conversion_info), 45.3592)
        self.assertEqual(convert(1000, conversion_info), 453.592)
        self.assertEqual(convert(-2, conversion_info), -0.90718)
        self.assertEqual(convert(-20, conversion_info), -9.0718)
        self.assertEqual(convert(-200, conversion_info), -90.718)
        self.assertEqual(convert(-2000, conversion_info), -907.18)
        self.assertEqual(convert(0, conversion_info), 0)
        self.assertEqual(convert(0.5, conversion_info), 0.2268)
        self.assertEqual(convert(0.05, conversion_info), 0.02268)
        self.assertEqual(convert(0.005, conversion_info), 0.00227)

    def test_g_to_kg(self):
        conversion_info = ("g to Kg", 0.001)
        self.assertEqual(convert(1, conversion_info), 0.001)
        self.assertEqual(convert(10, conversion_info), 0.01)
        self.assertEqual(convert(100, conversion_info), 0.1)
        self.assertEqual(convert(1000, conversion_info), 1)
        self.assertEqual(convert(-2, conversion_info), -0.002)
        self.assertEqual(convert(-20, conversion_info), -0.02)
        self.assertEqual(convert(-200, conversion_info), -0.2)
        self.assertEqual(convert(-2000, conversion_info), -2)
        self.assertEqual(convert(0, conversion_info), 0)
        self.assertEqual(convert(0.5, conversion_info), 0.0005)
        self.assertEqual(convert(0.05, conversion_info), 0.00005)
        self.assertEqual(convert(0.005, conversion_info), 0.00001)

    def test_g_to_lb(self):
        conversion_info = ("g to Lb", 0.00220462)
        self.assertEqual(convert(1, conversion_info), 0.0022)
        self.assertEqual(convert(10, conversion_info), 0.022)
        self.assertEqual(convert(100, conversion_info), 0.2205)
        self.assertEqual(convert(1000, conversion_info), 2.2046)
        self.assertEqual(convert(-2, conversion_info), -0.0044)
        self.assertEqual(convert(-20, conversion_info), -0.0441)
        self.assertEqual(convert(-200, conversion_info), -0.441)
        self.assertEqual(convert(-2000, conversion_info), -4.4092)
        self.assertEqual(convert(0, conversion_info), 0)
        self.assertEqual(convert(0.5, conversion_info), 0.0011)
        self.assertEqual(convert(0.05, conversion_info), 0.0001)
        self.assertEqual(convert(0.005, conversion_info), 0.00001)

    def test_g_to_oz(self):
        conversion_info = ("g to Oz", 0.035274)
        self.assertEqual(convert(1, conversion_info), 0.0353)
        self.assertEqual(convert(10, conversion_info), 0.3527)
        self.assertEqual(convert(100, conversion_info), 3.5274)
        self.assertEqual(convert(1000, conversion_info), 35.274)
        self.assertEqual(convert(-2, conversion_info), -0.0705)
        self.assertEqual(convert(-20, conversion_info), -0.7055)
        self.assertEqual(convert(-200, conversion_info), -7.055)
        self.assertEqual(convert(-2000, conversion_info), -70.55)
        self.assertEqual(convert(0, conversion_info), 0)
        self.assertEqual(convert(0.5, conversion_info), 0.0176)
        self.assertEqual(convert(0.05, conversion_info), 0.0018)
        self.assertEqual(convert(0.005, conversion_info), 0.0002)


if __name__ == "__main__":
    unittest.main()
