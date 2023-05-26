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
    obtained = pk.get_average(1, 3, 4)
    expected = [2.66]
    assert obtained == expected
