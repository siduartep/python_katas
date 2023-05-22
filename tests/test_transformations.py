import python_katas as pk


def test_add_offset():
    augend = 1
    addend = 2
    expected = augend + addend
    obtained = pk.add_offset(augend, addend)
    assert expected == obtained
