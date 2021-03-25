import takeltest

testinfra_hosts = takeltest.hosts()


def test_my_sidecar_role_default_variable(host, testvars):
    default_value = testvars['my_sidecar_role_default_key']

    assert 'my_default_value' == default_value
