from weight_converter_dropdown import num_separator


def test_num_separator():
    assert num_separator(1000) == "1,000"
    assert num_separator(123456789) == "123,456,789"
    assert num_separator(9876543210) == "9,876,543,210"
    assert num_separator(123) == "123"
    assert num_separator(0) == "0"
    print("All tests passed for num_separator()")


if __name__ == "__main__":
    test_num_separator()
