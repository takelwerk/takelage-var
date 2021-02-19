import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_env_role_procps_install_packages_installed(host, testvars):
    procps_packages = testvars['procps_packages']
    for debian_package in procps_packages:
        deb = host.package(debian_package)
        assert deb.is_installed
