import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_system_project_group(testvars):
    assert testvars['anarchism_group_vars_private_var'] \
           == 'my_group_vars_private_value'
