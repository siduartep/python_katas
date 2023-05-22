import python_katas as pk


def test_high_and_low():
    expected = "2 1"
    obtained = pk.high_and_low("2 1")
    assert obtained == expected
    expected = "3 2"
    obtained = pk.high_and_low("3 2")
    assert obtained == expected
    expected = "3 1"
    obtained = pk.high_and_low("3 2 1")
    assert obtained == expected
