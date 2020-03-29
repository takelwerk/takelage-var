import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_ruby_role_gpg_install_packages_installed(host, testvars):
    gpg_packages = testvars['gpg_packages']
    for debian_package in gpg_packages:
        deb = host.package(debian_package)
        assert deb.is_installed
