import pytest
import takeltest

def test_takeltest_unit_moleculebook_is_not_none(moleculebook):
    assert moleculebook is not None


def test_takeltest_unit_moleculebook_get(moleculebook):
    assert moleculebook.get() == moleculebook._playbook


def test_takeltest_unit_moleculebook_set(moleculebook):
    playbook = "\n---\n- name: localplay\n  hosts: localhost"
    moleculebook.set(playbook)
    assert moleculebook._playbook == playbook


def test_takeltest_unit_moleculebook_create_default(moleculebook):
    playbook_default = \
        {'name': 'ansible playbook',
         'hosts': 'localhost',
         'gather_facts': 'True',
         'vars_files': [],
         'roles': [],
         'tasks': []}
    moleculebook.create()
    playbook = moleculebook._playbook
    assert playbook == playbook_default


def test_takeltest_unit_moleculebook_create_extra_vars(
        moleculebook,
        monkeypatch):
    playbook_extra_vars = \
        {'name': 'ansible playbook',
         'hosts': 'localhost',
         'gather_facts': 'True',
         'vars_files': ['my_extra_vars.yml'],
         'roles': [],
         'tasks': []}
    monkeypatch.setattr(takeltest.moleculebook.MoleculeBook,
                        '_get_extra_vars_',
                        lambda x: ['my_extra_vars.yml'])
    moleculebook.create(extra_vars=True)
    playbook = moleculebook._playbook
    assert playbook == playbook_extra_vars


def test_takeltest_unit_moleculebook_create_gather_roles(
        moleculebook,
        monkeypatch):
    playbook_roles = \
        {'name': 'ansible playbook',
         'hosts': 'localhost',
         'gather_facts': 'True',
         'vars_files': [],
         'roles': [{'name': 'my_role', 'when': 'False'}],
         'tasks': []}
    monkeypatch.setattr(takeltest.moleculeplay.MoleculePlay,
                        'get_roles',
                        lambda x: ['my_role'])
    moleculebook.create(gather_roles=True)
    playbook = moleculebook._playbook
    assert playbook == playbook_roles


def test_takeltest_unit_moleculebook_add_task_debug_msg(moleculebook):
    moleculebook.create()
    moleculebook.add_task_debug_msg("Happy testing!")
    runner = moleculebook.run()
    for event in runner.events:
        try:
            msg = event['event_data']['res']['msg']
            break
        except (IndexError, KeyError):
            continue
    assert 'Happy testing!' == msg


def test_takeltest_unit_moleculebook_get_vars_default(moleculebook):
    vars = moleculebook.get_vars()
    assert 'localhost' in vars['inventory_hostname']


def test_takeltest_unit_moleculebook_run_task_get_vars(moleculebook):
    moleculebook.create()
    playbook = moleculebook.get()
    playbook = playbook | {'vars': {'myvar': 'myvalue', 'myvarref': '{{ myvar }}'}}
    playbook['gather_facts'] = 'False'
    moleculebook.set(playbook)
    vars = moleculebook.get_vars()
    assert vars['myvarref'] == 'myvalue'


def test_takeltest_unit_moleculebook_add_task_include_vars_dir(moleculebook):
    playbook_task_debug = \
        {'name': 'ansible playbook',
         'hosts': 'localhost',
         'gather_facts': 'True',
         'vars_files': [],
         'roles': [],
         'tasks': [{'action': {'module': 'include_vars',
                               'args': {'dir': 'my_custom_vars'}}}]}
    moleculebook.create()
    moleculebook.add_task_include_vars_dir("my_custom_vars")
    playbook = moleculebook._playbook
    assert playbook == playbook_task_debug


def test_takeltest_unit_moleculebook_run(moleculebook, monkeypatch):
    monkeypatch.setattr(takeltest.moleculeplay.MoleculePlay,
                        'run_playbook',
                        lambda x, y: 'my_playbook_result')
    playbook_result = moleculebook.run()
    assert playbook_result == 'my_playbook_result'


def test_takeltest_unit_get_molecule_scenario_directory(moleculebook):
    moleculeplay_mcd = \
        moleculebook._moleculeplay.get_molecule_scenario_directory()
    moleculebook_mcd = \
        moleculebook._get_molecule_scenario_directory_()
    assert moleculebook_mcd == moleculeplay_mcd


def test_takeltest_unit_moleculebook_testvars_extra_vars_no_files(
        moleculebook):
    files = moleculebook._get_extra_vars_()
    assert files == []
