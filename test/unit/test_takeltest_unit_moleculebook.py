import takeltest


def test_takeltest_unit_moleculebook_is_not_none(moleculebook):
    assert moleculebook is not None


def test_takeltest_unit_moleculebook_get(moleculebook):
    assert moleculebook.get() == moleculebook._playbook


def test_takeltest_unit_moleculebook_set(moleculebook):
    playbook = "\n---\n- name: localplay\n  hosts: localhost"
    moleculebook.set(playbook)
    assert playbook == moleculebook._playbook


def test_takeltest_unit_moleculebook_create_default(moleculebook):
    playbook_default = \
        [{'name': 'ansible playbook',
          'hosts': 'localhost',
          'gather_facts': 'False',
          'vars_files': [],
          'roles': [],
          'tasks': []}]
    moleculebook.create()
    playbook = moleculebook._playbook
    assert playbook_default == playbook


def test_takeltest_unit_moleculebook_create_extra_vars(
        moleculebook,
        monkeypatch):
    playbook_extra_vars = \
        [{'name': 'ansible playbook',
          'hosts': 'localhost',
          'gather_facts': 'False',
          'vars_files': ['my_extra_vars.yml'],
          'roles': [],
          'tasks': []}]
    monkeypatch.setattr(takeltest.moleculebook.MoleculeBook,
                        '_get_extra_vars_',
                        lambda x: ['my_extra_vars.yml'])
    moleculebook.create(extra_vars=True)
    playbook = moleculebook._playbook
    assert playbook_extra_vars == playbook


def test_takeltest_unit_moleculebook_create_gather_roles(
        moleculebook,
        monkeypatch):
    playbook_roles = \
        [{'name': 'ansible playbook',
          'hosts': 'localhost',
          'gather_facts': 'False',
          'vars_files': [],
          'roles': [{'name': 'my_role', 'when': 'False'}],
          'tasks': []}]
    monkeypatch.setattr(takeltest.moleculebook.MoleculeBook,
                        'get_roles',
                        lambda x: ['my_role'])
    moleculebook.create(gather_roles=True)
    playbook = moleculebook._playbook
    assert playbook_roles == playbook


def test_takeltest_unit_moleculebook_add_task_debug_msg(moleculebook):
    msg = ''
    moleculebook.create()
    moleculebook.set(moleculebook.add_task_debug_msg(
        'Happy testing!', moleculebook.get(), 'add_task_debug_msg'))
    runner = moleculebook.run(moleculebook.get())
    for event in runner.events:
        try:
            if event['event'] == 'runner_on_ok':
                if event['event_data']['task'] == 'add_task_debug_msg':
                    msg = event['event_data']['res']['msg']
                    break
        except (IndexError, KeyError):
            continue
    assert 'Happy testing!' == msg


def test_takeltest_unit_moleculebook_get_vars_default(moleculebook):
    vars = moleculebook.get_vars('localhost')
    assert 'localhost' in vars['inventory_hostname']


def test_takeltest_unit_moleculebook_add_task_include_vars_dir(moleculebook):
    playbook_task_debug = \
        [{'name': 'ansible playbook',
          'hosts': 'localhost',
          'gather_facts': 'False',
          'vars_files': [],
          'roles': [],
          'tasks': [
              {'name': 'add_task_include_vars_dir',
               'ansible.builtin.include_vars': {
                   'dir': 'my_custom_vars'}}]}]
    moleculebook.create()
    moleculebook.set(moleculebook.add_task_include_vars_dir(
        'my_custom_vars', moleculebook.get(), 'add_task_include_vars_dir'))
    playbook = moleculebook._playbook
    assert playbook_task_debug == playbook


def test_takeltest_unit_moleculebook_testvars_extra_vars_no_files(
        moleculebook):
    files = moleculebook._get_extra_vars_()
    assert files == []
