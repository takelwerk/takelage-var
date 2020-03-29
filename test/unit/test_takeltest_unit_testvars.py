import pytest
import re
import takeltest
from takeltest.testvars import TestVars
from takeltest.exceptions import AnsibleRunError


def test_takeltest_unit_testvars_is_not_none(
        moleculelog,
        debug_jsonvars,
        moleculebook,
        jsonvars,
        gather_facts,
        extra_vars):
    with pytest.raises(AnsibleRunError):
        TestVars(moleculelog,
                 debug_jsonvars,
                 moleculebook,
                 jsonvars,
                 gather_facts,
                 extra_vars).get_testvars()


def test_takeltest_unit_testvars_resolve_vars(
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
    monkeypatch.setattr(takeltest.moleculebook.MoleculeBook,
                        'get_vars',
                        lambda w, x, y: testvars_unresolved)
    monkeypatch.setattr(takeltest.jsonvars.JsonVars,
                        'resolve',
                        lambda x: None)
    monkeypatch.setattr(takeltest.jsonvars.JsonVars,
                        'get',
                        lambda x: jsonvars_resolved)
    gather_facts = False
    extra_vars = ''
    testvars = TestVars(moleculelog,
                        debug_jsonvars,
                        moleculebook,
                        jsonvars,
                        gather_facts,
                        extra_vars).get_testvars()
    assert testvars == testvars_resolved


def test_takeltest_unit_testvars_cache_key(cache_key):
    assert re.match('testvars/+', cache_key)
