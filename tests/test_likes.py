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
    obtained = pk.likes(["Juanita", "Jacob"])
    expected = "Juanita and Jacob like this"
    assert obtained == expected
    obtained = pk.likes(["Max", "John", "Mark"])
    expected = "Max, John and Mark like this"
    assert obtained == expected
    obtained = pk.likes(["Alex", "Jacob", "Mark", "Max"])
    expected = "Alex, Jacob and 2 others like this"
    assert obtained == expected
