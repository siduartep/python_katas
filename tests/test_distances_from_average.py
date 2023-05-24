import python_katas as pk


def test_distances_from_average():
    obtained = [1, 2, 3]
    expected = pk.distances_from_average([1, 2, 3])
    assert obtained == expected
