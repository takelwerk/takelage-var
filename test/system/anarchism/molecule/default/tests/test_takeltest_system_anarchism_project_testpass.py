# import mock
import takeltest

testinfra_hosts = takeltest.hosts()

# @mock.patch('takeltest.moleculebook.MoleculeBook.run',
#             return_value=[{'msg':'my_secret_value'}])
# def test_takeltest_system_testpass_mock(host, testpass):
#      my_secret_value = testpass('my_secret_key')
#      assert my_secret_value == 'my_secret_value'


def test_takeltest_system_testpass_monkeypatch(host, monkeypatch, testpass):
    monkeypatch.setattr(takeltest.moleculebook.MoleculeBook, 'run',
                        lambda x: [{'msg': 'my_secret_value'}])
    my_secret_value = testpass('my_secret_key')
    assert my_secret_value == 'my_secret_value'
