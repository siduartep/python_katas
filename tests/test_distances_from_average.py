import python_katas as pk


def test_distances_from_average():
    obtained = pk.distances_from_average([0])
    expected = [0]
    assert obtained == expected
    obtained = pk.distances_from_average([1])
    expected = [0]
    assert obtained == expected


def test_get_average():
    obtained = pk.get_average([0])
    expected = [0]
    assert obtained == expected
    obtained = pk.get_average([1])
    expected = [1]
    assert obtained == expected
    obtained = pk.get_average([1, 3])
    expected = [2]
    assert obtained == expected
    obtained = pk.get_average([1, 3, 4])
    expected = [2.67]
    assert obtained == expected


def test_total():
    obtained = pk.distances_from_average([2, 2])
    expected = [0, 0]
    assert obtained == expected
    obtained = pk.distances_from_average([123, -65, 32432, -353, -534])
    expected = [6197.6, 6385.6, -26111.4, 6673.6, 6854.6]
    assert obtained == expected
