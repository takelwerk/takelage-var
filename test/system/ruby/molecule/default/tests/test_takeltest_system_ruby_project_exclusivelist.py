import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_ruby_project_test_exclusivelist_curl_and_vim(host, testvars):
    assert 'curl_packages' in testvars
    assert 'vim_packages' in testvars
    assert 'gpg_packages' not in testvars
    assert 'procps_packages' not in testvars
