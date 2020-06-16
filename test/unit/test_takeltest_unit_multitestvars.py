import pytest
import re
import takeltest
from takeltest.multitestvars import MultiTestVars
from takeltest.exceptions import AnsibleRunError


def test_takeltest_unit_multitestvars_is_not_none(
        ansibleinventory,
        moleculelog,
        debug_jsonvars,
        moleculebook,
        jsonvars,
        gather_facts,
        extra_vars):
    with pytest.raises(AnsibleRunError):
        MultiTestVars(
            ansibleinventory,
            moleculelog,
            debug_jsonvars,
            moleculebook,
            jsonvars,
            gather_facts,
            extra_vars).get_testvars()


def test_takeltest_unit_multitestvars_resolve_vars(
        ansibleinventory,
        moleculelog,
        debug_jsonvars,
        moleculebook,
        jsonvars,
        monkeypatch):
    testvars_unresolved = \
        {'my_var_1': 'my_value', 'my_var_2': '{{ my_var_1 }}'}
    jsonvars_resolved = \
        '{"my_var_1": "my_value", "my_var_2": "my_value"}'
    testvars_resolved = \
        {'my_var_1': 'my_value', 'my_var_2': 'my_value'}
    monkeypatch.setattr(
        takeltest.moleculebook.MoleculeBook,
        'get_vars',
        lambda w, x, y, z: testvars_unresolved)
    monkeypatch.setattr(
        takeltest.jsonvars.JsonVars,
        'resolve',
        lambda x: None)
    monkeypatch.setattr(
        takeltest.jsonvars.JsonVars,
        'get',
        lambda x: jsonvars_resolved)
    gather_facts = False
    extra_vars = ''
    multitestvars = MultiTestVars(
        ansibleinventory,
        moleculelog,
        debug_jsonvars,
        moleculebook,
        jsonvars,
        gather_facts,
        extra_vars).get_multitestvars()
    assert multitestvars['localhost'] == testvars_resolved


def test_takeltest_unit_multitestvars_cache_key(cache_key):
    assert re.match('multitestvars/+', cache_key)
