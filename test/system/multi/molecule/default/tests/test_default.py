import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_multi_hostname(multitestvars, testvars):
    assert not multitestvars['molecule-takeltest-multi-first']['example_var']
    assert multitestvars['molecule-takeltest-multi-second']['example_var']
    assert testvars['ansible_facts']['hostname'] == \
           'molecule-takeltest-multi-first'
