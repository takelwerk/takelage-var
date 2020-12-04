import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_ruby_project_test_ruby(host):
    assert host.run('ruby')


def test_takeltest_ruby_project_test_blocklist_vim(host, testvars):
    assert 'vim_packages' in testvars
