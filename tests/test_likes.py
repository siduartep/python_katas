import python_katas as pk


def test_likes():
    obtained = pk.likes([])
    expected = "no one likes this"
    assert obtained == expected
    obtained = pk.likes(["Peter"])
    expected = "Peter likes this"
    assert obtained == expected
    obtained = pk.likes(["Jacob", "Alex"])
    expected = "Jacob and Alex like this"
    assert obtained == expected
