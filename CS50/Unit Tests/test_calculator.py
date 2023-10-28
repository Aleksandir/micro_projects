from calculator import square


def test_square():
    assert square(10) == 100
    assert square(2.5) == 6.25
    assert square(-10) == 100
    assert square(0) == 0
    print("All tests passed for square()")
