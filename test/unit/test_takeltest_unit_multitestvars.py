import re
import takeltest
from takeltest.multitestvars import MultiTestVars


def test_takeltest_unit_multitestvars_cache_key(cache_key):
    assert re.match('multitestvars/+', cache_key)


def test_takeltest_unit_multitestvars_resolve_vars(
        moleculeinventory,
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
        lambda x, y, z: testvars_unresolved)
    monkeypatch.setattr(
        takeltest.jsonvars.JsonVars,
        'resolve',
        lambda x: None)
    monkeypatch.setattr(
        takeltest.jsonvars.JsonVars,
        'get',
        lambda x: jsonvars_resolved)
    extra_vars = ''
    multitestvars = MultiTestVars(
        moleculeinventory,
        moleculelog,
        debug_jsonvars,
        moleculebook,
        jsonvars,
        extra_vars).get_multitestvars()
    assert multitestvars['localhost'] == testvars_resolved
