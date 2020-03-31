import re
import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_anarchism_configure_root_bashrc(host, testvars):
    if 'fortune-anarchism' in testvars['takel_anarchism_deb_install_packages']:
        with host.sudo():
            file = host.file('/root/.bashrc')
            expected = '''
echo
/usr/games/fortune -s anarchism
echo
'''
            assert re.search(expected, file.content_string) is not None
