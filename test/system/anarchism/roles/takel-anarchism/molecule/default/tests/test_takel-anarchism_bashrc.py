import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_anarchism_bashrc_source(host, testvars):
    if 'fortune-anarchism' in testvars['takel_anarchism_deb_install_packages']:
        with host.sudo():
            file = host.file('/root/.bashrc')
            expected = '''\
if [ -d .bashrc.d ]; then
  for i in .bashrc.d/*; do
    if [ -r $i ]; then
      . $i
    fi
  done
  unset i
fi
'''
            assert expected in file.content_string


def test_takel_anarchism_bashrc_directory(host, testvars):
    if 'fortune-anarchism' in testvars['takel_anarchism_deb_install_packages']:
        with host.sudo():
            dir = host.file('/root/.bashrc.d')

            assert dir.exists
            assert dir.is_directory
            assert dir.user == 'root'
            assert dir.group == 'root'
            assert dir.mode == 0o755


def test_takel_anarchism_bashrc_files(host, testvars):
    if 'fortune-anarchism' in testvars['takel_anarchism_deb_install_packages']:
        bashrc_files = testvars['takel_anarchism_bashrc']
        for bashrc_file in bashrc_files:
            with host.sudo():
                file = host.file(f"/root/.bashrc.d/{bashrc_file}")
                assert file.exists
                assert file.is_file
                assert file.user == 'root'
                assert file.group == 'root'
                assert file.mode == 0o644
