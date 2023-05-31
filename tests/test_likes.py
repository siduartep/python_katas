import python_katas as pk


def test_likes():
    obtained = pk.likes([])
    expected = "no one likes this"
    assert obtained == expected
