import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_ruby_role_curl_system(host):
    assert host.run('curl')
