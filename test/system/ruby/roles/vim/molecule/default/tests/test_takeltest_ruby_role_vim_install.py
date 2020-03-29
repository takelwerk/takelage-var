import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_ruby_role_vim_install_packages_installed(host, testvars):
    vim_packages = testvars['vim_packages']
    for debian_package in vim_packages:
        deb = host.package(debian_package)
        assert deb.is_installed
