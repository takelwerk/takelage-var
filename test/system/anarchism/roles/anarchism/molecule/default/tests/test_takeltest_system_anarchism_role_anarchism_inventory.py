import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_system_role_inventory(host, testvars):
    assert testvars['anarchism_group_vars_all'] == 'my_group_vars_all_value'
