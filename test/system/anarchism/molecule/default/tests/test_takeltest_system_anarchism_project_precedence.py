import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_system_precedence_can_read_role_default(host, testvars):
    assert testvars['anarchism_install']


def test_takeltest_system_precedence_project_over_role_default(host, testvars):
    expected = ['anarchism', 'fortune-anarchism']
    assert testvars['anarchism_packages'] == expected
