import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_env_role_procps_system(host):
    assert host.run('ps')
