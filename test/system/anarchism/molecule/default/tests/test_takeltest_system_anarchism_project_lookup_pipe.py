import takeltest

testinfra_hosts = takeltest.hosts()


import pytest
@pytest.mark.run_this_only
def test_takeltest_system_project_lookup_pipe(testvars):
    project = testvars['project']
    print(project)
    print(type(project))
    assert 'pytest-takeltest' == project['name']
