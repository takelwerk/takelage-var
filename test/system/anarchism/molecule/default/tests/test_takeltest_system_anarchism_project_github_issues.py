import takeltest

testinfra_hosts = takeltest.hosts()


# issue: https://github.com/RebelCodeBase/takeltest/issues/1
def test_takeltest_system_github_issues_1(host, testvars):
    assert testvars['project_github_issues_1_file'] == 'bar'
