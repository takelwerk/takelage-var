import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_multi_hostname(host, testvars):
    hostname = host.run("hostname").stdout.strip()
    example_var = testvars['example_var']

    if hostname == 'molecule-takeltest-multi-default-first':
        assert not example_var
    elif hostname == 'molecule-takeltest-multi-default-second':
        assert example_var
    else:
        assert False, 'Unknown host'
