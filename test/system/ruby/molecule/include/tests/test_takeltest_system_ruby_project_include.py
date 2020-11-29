import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_ruby_project_test_include(host, testvars):
    assert 'curl_packages' in testvars
    assert 'gpg_packages' in testvars
    assert 'vim_packages' in testvars
