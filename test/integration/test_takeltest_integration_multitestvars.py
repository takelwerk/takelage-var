from takeltest.multitestvars import MultiTestVars

from pprint import pformat
from typing import Any
from pygments import highlight
from pygments.formatters import Terminal256Formatter
from pygments.lexers import PythonLexer
def pprint_color(obj: Any) -> None:
    """Pretty-print in color."""
    print(highlight(pformat(obj), PythonLexer(), Terminal256Formatter()), end="")

def test_takeltest_unit_multitestvars_resolve_vars_ansible(
        moleculeinventory,
        moleculelog,
        debug_jsonvars,
        moleculebook,
        jsonvars):
    moleculebook.create()
    playbook = moleculebook.get()
    playbook = playbook | {'vars': {'myvar': 'myvalue', 'myvarref': '{{ myvar }}'}}
    moleculebook.set(playbook)
    extra_vars = ''
    multitestvars = MultiTestVars(
        moleculeinventory,
        moleculelog,
        debug_jsonvars,
        moleculebook,
        jsonvars,
        extra_vars).get_multitestvars()
    assert multitestvars['localhost']['myvarref'] == 'myvalue'
