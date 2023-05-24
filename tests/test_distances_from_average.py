import python_katas as pk


def test_distances_from_average():
    expected = [0]
    obtained = pk.distances_from_average([0])
    assert obtained == expected
    expected = [0]
    obtained = pk.distances_from_average([1])
    assert obtained == expected
    expected = [0, 0]
    obtained = pk.distances_from_average([2, 2])
    assert obtained == expected
