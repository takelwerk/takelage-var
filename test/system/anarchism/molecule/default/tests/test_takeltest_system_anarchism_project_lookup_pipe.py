import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_system_project_lookup_pipe(testvars):
    project = testvars['project']
    assert 'pytest-takeltest' == project['name']
