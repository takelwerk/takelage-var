import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_env_project_test_env(host):
    assert host.run('ps')


def test_takeltest_env_project_test_blocklist_gpg_vim(host, testvars):
    assert 'gpg_packages' not in testvars
    assert 'vim_packages' not in testvars
