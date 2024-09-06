import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_system_ansiblefacts_present(host, testvars):
    assert 'ansible_distribution_version' in testvars


def test_takeltest_system_ansiblefacts_reference(host, testvars):
    assert type(testvars['project_factref']) is str
