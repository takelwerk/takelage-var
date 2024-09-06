def test_takeltest_unit_moleculeinventory_is_not_none(moleculeinventory):
    assert moleculeinventory is not None


def test_takeltest_unit_moleculeinventory_hosts(moleculeinventory):
    assert moleculeinventory.hosts() == ['localhost']
