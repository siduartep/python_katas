import python_katas as pk


def test_high_and_low():
    expected = "2 1"
    obtained = pk.high_and_low("2 1")
    assert obtained == expected
    expected = "3 2"
    obtained = pk.high_and_low("3 2")
    assert obtained == expected
    expected = "3 1"
    obtained = pk.high_and_low("1 3")
    assert obtained == expected
    expected = "42 -9"
    obtained = pk.high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
    assert obtained == expected
