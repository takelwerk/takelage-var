import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_system_ruby_role_var(host, testvars):
    assert testvars['vim_my_role_var'] == 'my_role_value'
