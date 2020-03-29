import takeltest


def test_takeltest_unit_testpass_is_not_none(testpass):
    assert testpass is not None


def test_takeltest_unit_testpass_returns_secret(
        testpass,
        monkeypatch):
    monkeypatch.setattr(takeltest.moleculebook.MoleculeBook,
                        'run',
                        lambda x: [{'msg': 'my_secret'}])
    my_secret = testpass('my_path/my_var')
    assert my_secret == 'my_secret'
