import takeltest
import pytest

testinfra_hosts = takeltest.hosts()


def test_takeltest_system_precedence_can_read_role_default(testvars):
    assert testvars['takel_anarchism_bashrc_d']


def test_takeltest_system_precedence_can_read_overwritten_role_default(testvars):
    assert testvars['takel_anarchism_deb_install_packages']


def test_takeltest_system_precedence_project_over_role_default(testvars):
    expected = ['anarchism', 'fortune-anarchism', 'sudo']
    assert testvars['takel_anarchism_deb_install_packages'] == expected
