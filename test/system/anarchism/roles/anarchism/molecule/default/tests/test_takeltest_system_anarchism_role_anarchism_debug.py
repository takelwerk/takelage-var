import pytest
from ruamel.yaml import YAML
import sys
import takeltest

testinfra_hosts = takeltest.hosts()
yaml = YAML()

# print testvars as yaml
# @pytest.mark.debug
@pytest.mark.skip
def test_takeltest_system_role_debug(host, testvars, testpass):
    print('\n*******************')
    yaml.dump(testvars, sys.stdout)
    print('*******************\n')
    assert False
