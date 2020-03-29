import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_ruby_project_test_ruby(host):
    assert host.run('ruby')


def test_takeltest_ruby_project_test_blacklist_vim(host, testvars):
    assert 'vim_packages' not in testvars
