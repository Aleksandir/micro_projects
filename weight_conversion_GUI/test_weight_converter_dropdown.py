from weight_converter_dropdown import convert


def test_convert():
    conversion_table = {
        "Kg to Lb": 2.20462,
        "Lb to Kg": 0.453592,
    }
    assert convert("Kg to Lb", 10, conversion_table) == "22.0 Lb"
    assert convert("Lb to Kg", 22, conversion_table) == "10.0 Kg"
    assert convert("Kg to Lb", 0.5, conversion_table) == "1.1 Lb"
    assert convert("Lb to Kg", 1.1, conversion_table) == "0.5 Kg"
    assert convert("Kg to Lb", 0, conversion_table) == "0 Lb"
    assert convert("Lb to Kg", 0, conversion_table) == "0 Kg"
    assert convert("Kg to Lb", -10, conversion_table) == "-22.0 Lb"
    assert convert("Lb to Kg", -22, conversion_table) == "-10.0 Kg"
    assert convert("Kg to Lb", 0.453592, conversion_table) == "1.0 Lb"
    assert convert("Lb to Kg", 2.20462, conversion_table) == "1.0 Kg"
    print("All tests passed for convert()")


if __name__ == "__main__":
    test_convert()
