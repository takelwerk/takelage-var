import json
import pytest
from takeltest.exceptions import AnsibleRunError


def test_takeltest_unit_moleculeplay_is_not_none(moleculeplay):
    assert moleculeplay is not None


def test_takeltest_unit_moleculeplay_exception_moleculeplayrunerror():
    label = 'my_label'
    result = ['my_result']
    with pytest.raises(AnsibleRunError) as excinfo:
        raise AnsibleRunError(label, json.dumps(result, indent=4))
    exception_msg = excinfo.value.args[0]
    assert exception_msg == 'my_label\n[\n    "my_result"\n]'


def test_takeltest_unit_moleculeplay_run_playbook_minimal(moleculeplay):
    playbook_minimal = \
        {'name': 'ansible minimal playbook',
         'hosts': 'localhost',
         'gather_facts': 'False'}
    result = moleculeplay.run_playbook(playbook_minimal)
    assert result == 0


def test_takeltest_unit_moleculeplay_run_playbook_debug(moleculeplay):
    args = dict(msg='hello world')
    task_debug = dict(action=dict(module='ansible.builtin.debug', args=args))
    playbook_debug = \
        {
            'name': 'ansible debug playbook',
            'hosts': 'localhost',
            'gather_facts': 'False',
            'tasks': [ task_debug ]
         }
    result = moleculeplay.run_playbook(playbook_debug)
    assert result == 0
