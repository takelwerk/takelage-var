import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_system_simple_true(host):
    assert True
