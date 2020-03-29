import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_ruby_role_vim_system(host):
    assert host.run('vim --version')
