import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_anarchism_system_fortune_greeting(host, testvars):
    if 'fortune-anarchism' in testvars['takel_anarchism_deb_install_packages']:
        with host.sudo():
            output = host.check_output('bash -c ". /root/.bashrc"')
            assert '-- ' in output


def test_takel_root_system_includes_alias(host):
    with host.sudo():
        output = host.check_output('bash -i -c "alias"')
        assert 'alias l=' in output
