import takeltest
import pytest

testinfra_hosts = takeltest.hosts()


def test_takeltest_system_varsfiles_project_vars(host, testvars):
    assert testvars['project_my_project_var'] == 'my_project_value'


def test_takeltest_system_varsfiles_extra_vars(host, testvars):
    assert testvars['project_my_extra_var'] == 'my_extra_value'


def test_takeltest_system_varsfiles_second_file_in_vars_dir(host, testvars):
    assert testvars['project_my_custom_var'] == 'my_custom_value'
