import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_vault_encryption(testvars):
    assert testvars['my_vault_key'] == 'my_vault_value'
