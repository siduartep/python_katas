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
