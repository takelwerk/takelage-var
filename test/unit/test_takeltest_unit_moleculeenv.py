from pathlib import Path
import takeltest
from takeltest.moleculeenv import MoleculeEnv


def test_takeltest_unit_moleculeenv_is_not_none(moleculeenv):
    assert moleculeenv is not None
    assert moleculeenv.get_roles() == list()


def test_takeltest_unit_moleculeenv_get_molecule_ephemeral_directory(
        moleculeenv,
        monkeypatch):
    med = moleculeenv.get_molecule_ephemeral_directory()
    assert med == moleculeenv._molecule_ephemeral_directory


def test_takeltest_unit_moleculeenv_get_molecule_scenario_directory(
        moleculeenv,
        monkeypatch):
    msd = moleculeenv.get_molecule_scenario_directory()
    assert msd == moleculeenv._molecule_scenario_directory


def test_takeltest_unit_moleculeenv_get_roles(
        moleculeenv,
        monkeypatch,
        tmp_path):
    my_roles = ['my_role_1', 'my_role_2']
    roles_dir = tmp_path / 'roles'
    roles_dir.mkdir()
    my_role_1 = roles_dir / 'my_role_1'
    my_role_1.mkdir()
    my_role_2 = roles_dir / 'my_role_2'
    my_role_2.mkdir()
    monkeypatch.setattr(takeltest.moleculeenv.MoleculeEnv,
                        'get_molecule_ephemeral_directory',
                        lambda x: tmp_path)
    roles = moleculeenv.get_roles()
    assert roles == my_roles


def test_takeltest_unit_moleculeenv_create_symlinks(
        moleculeenv,
        monkeypatch,
        tmp_path):
    med = tmp_path / 'molecule_ephemeral_directory'
    med.mkdir()
    roles_dir = tmp_path / 'roles'
    roles_dir.mkdir()
    monkeypatch.setattr(takeltest.moleculeenv.MoleculeEnv,
                        'get_molecule_ephemeral_directory',
                        lambda x: med)
    monkeypatch.setattr(takeltest.moleculeenv.MoleculeEnv,
                        'get_project_dir',
                        lambda x: tmp_path)
    moleculeenv._create_symlink_('roles')
    assert (med / 'roles').is_symlink()


def test_takeltest_unit_moleculeenv_create_symlinks_fileexistserror(
        moleculeenv,
        monkeypatch,
        tmp_path):
    med = tmp_path / 'molecule_ephemeral_directory'
    med.mkdir()
    roles_dir = tmp_path / 'roles'
    roles_dir.mkdir()
    monkeypatch.setattr(takeltest.moleculeenv.MoleculeEnv,
                        'get_molecule_ephemeral_directory',
                        lambda x: med)
    monkeypatch.setattr(takeltest.moleculeenv.MoleculeEnv,
                        'get_project_dir',
                        lambda x: tmp_path)

    # create symlink twice
    moleculeenv._create_symlink_('roles')
    moleculeenv._create_symlink_('roles')
    assert (med / 'roles').is_symlink()


def test_takeltest_unit_moleculeenv_get_project_dir(
        moleculeenv,
        monkeypatch,
        tmp_path):
    msd = tmp_path / 'roles/my_role/molecule/default'
    msd.mkdir(parents=True)
    monkeypatch.setattr(takeltest.moleculeenv.MoleculeEnv,
                        'get_molecule_scenario_directory',
                        lambda x: msd)
    project_dir = moleculeenv.get_project_dir()
    assert project_dir == tmp_path


def test_takeltest_unit_moleculeenv_get_project_dir_no_roles_dir(
        moleculeenv,
        monkeypatch):
    monkeypatch.setattr(takeltest.moleculeenv.MoleculeEnv,
                        'get_molecule_scenario_directory',
                        lambda x: Path('/'))
    project_dir = moleculeenv.get_project_dir()
    assert project_dir is None


def test_takeltest_unit_moleculeenv_no_gather_roles(tmp_path):
    my_playbook = """\
---
- name: converge
  hosts: all
  gather_facts: false
  roles:
    - my_role
"""
    med = tmp_path / 'molecule_ephemeral_directory'
    med.mkdir()

    msd = tmp_path / 'molecule_scenario_directory'
    msd.mkdir()

    (tmp_path / 'roles' / 'my_role').mkdir(parents=True)

    playbook_path = msd / 'playbook.yml'
    playbook_path.write_text(my_playbook)

    gather_roles = False
    testvars_roles_blocklist = []
    testvars_roles_exclusivelist = []
    testvars_roles_includelist = []
    testvars_roles_playbooks = []

    moleculeenv = MoleculeEnv(med,
                              msd,
                              gather_roles,
                              testvars_roles_blocklist,
                              testvars_roles_exclusivelist,
                              testvars_roles_includelist,
                              testvars_roles_playbooks)

    assert moleculeenv.get_roles() == []


def test_takeltest_unit_moleculeenv_roles_from_custom_converge_playboook(
        tmp_path):
    my_molecule_yml = """\
---
provisioner:
    name: ansible
    playbooks:
        converge: my_playbook.yml
"""
    my_playbook = """\
---
- name: converge
  hosts: all
  gather_facts: false
  roles:
    - my_role
"""
    med = tmp_path / 'molecule_ephemeral_directory'
    med.mkdir()

    msd = tmp_path / 'molecule_scenario_directory'
    msd.mkdir()

    (tmp_path / 'roles' / 'my_role').mkdir(parents=True)

    molecule_yml_path = msd / 'molecule.yml'
    molecule_yml_path.write_text(my_molecule_yml)

    playbook_path = msd / 'my_playbook.yml'
    playbook_path.write_text(my_playbook)

    gather_roles = True
    testvars_roles_blocklist = []
    testvars_roles_exclusivelist = []
    testvars_roles_includelist = []
    testvars_roles_playbooks = []

    moleculeenv = MoleculeEnv(med,
                              msd,
                              gather_roles,
                              testvars_roles_blocklist,
                              testvars_roles_exclusivelist,
                              testvars_roles_includelist,
                              testvars_roles_playbooks)

    assert moleculeenv.get_roles() == ['my_role']


def test_takeltest_unit_moleculeenv_roles_from_playboook_expand_path(
        monkeypatch,
        tmp_path):
    monkeypatch.setenv(
        'TAKELAGE_MOLECULE_CONVERGE_PLAYBOOK',
        'my_playbook.yml')

    my_molecule_yml = """\
---
provisioner:
    name: ansible
    playbooks:
        converge: >-
          ${TAKELAGE_MOLECULE_CONVERGE_PLAYBOOK:-custom-playbook.yml}
"""
    my_playbook = """\
---
- name: converge
  hosts: all
  gather_facts: false
  roles:
    - my_role
"""
    med = tmp_path / 'molecule_ephemeral_directory'
    med.mkdir()

    msd = tmp_path / 'molecule_scenario_directory'
    msd.mkdir()

    (tmp_path / 'roles' / 'my_role').mkdir(parents=True)

    molecule_yml_path = msd / 'molecule.yml'
    molecule_yml_path.write_text(my_molecule_yml)

    playbook_path = msd / 'my_playbook.yml'
    playbook_path.write_text(my_playbook)

    gather_roles = True
    testvars_roles_blocklist = []
    testvars_roles_exclusivelist = []
    testvars_roles_includelist = []
    testvars_roles_playbooks = []

    moleculeenv = MoleculeEnv(med,
                              msd,
                              gather_roles,
                              testvars_roles_blocklist,
                              testvars_roles_exclusivelist,
                              testvars_roles_includelist,
                              testvars_roles_playbooks)

    assert moleculeenv.get_roles() == ['my_role']


def test_takeltest_unit_moleculeenv_roles_from_default_converge_playboook(
        tmp_path):
    my_playbook = """\
---
- name: converge
  hosts: all
  gather_facts: false
  roles:
    - my_role
"""
    med = tmp_path / 'molecule_ephemeral_directory'
    med.mkdir()

    msd = tmp_path / 'molecule_scenario_directory'
    msd.mkdir()

    (tmp_path / 'roles' / 'my_role').mkdir(parents=True)

    playbook_path = msd / 'playbook.yml'
    playbook_path.write_text(my_playbook)

    gather_roles = True
    testvars_roles_blocklist = []
    testvars_roles_exclusivelist = []
    testvars_roles_includelist = []
    testvars_roles_playbooks = []

    moleculeenv = MoleculeEnv(med,
                              msd,
                              gather_roles,
                              testvars_roles_blocklist,
                              testvars_roles_exclusivelist,
                              testvars_roles_includelist,
                              testvars_roles_playbooks)

    assert moleculeenv.get_roles() == ['my_role']


def test_takeltest_unit_moleculeenv_get_roles_not_blocklisted(tmp_path):
    my_playbook = """\
---
- name: converge
  hosts: all
  gather_facts: false
  roles:
    - my_role_1
    - my_role_2
"""
    my_roles = ['my_role_2']

    med = tmp_path / 'molecule_ephemeral_directory'
    med.mkdir()

    msd = tmp_path / 'molecule_scenario_directory'
    msd.mkdir()

    my_role_1 = tmp_path / 'roles' / 'my_role_1'
    my_role_1.mkdir(parents=True)

    my_role_2 = tmp_path / 'roles' / 'my_role_2'
    my_role_2.mkdir()

    playbook_path = msd / 'playbook.yml'
    playbook_path.write_text(my_playbook)

    gather_roles = True
    testvars_roles_blocklist = ['my_role_1']
    testvars_roles_exclusivelist = []
    testvars_roles_includelist = []
    testvars_roles_playbooks = []

    moleculeenv = MoleculeEnv(med,
                              msd,
                              gather_roles,
                              testvars_roles_blocklist,
                              testvars_roles_exclusivelist,
                              testvars_roles_includelist,
                              testvars_roles_playbooks)

    assert moleculeenv.get_roles() == my_roles


def test_takeltest_unit_moleculeenv_get_roles_exclusivelisted(tmp_path):
    my_playbook = """\
---
- name: converge
  hosts: all
  gather_facts: false
  roles:
    - my_role_1
    - my_role_2
"""
    my_roles = ['my_role_2']

    med = tmp_path / 'molecule_ephemeral_directory'
    med.mkdir()

    msd = tmp_path / 'molecule_scenario_directory'
    msd.mkdir()

    my_role_1 = tmp_path / 'roles' / 'my_role_1'
    my_role_1.mkdir(parents=True)

    my_role_2 = tmp_path / 'roles' / 'my_role_2'
    my_role_2.mkdir()

    playbook_path = msd / 'playbook.yml'
    playbook_path.write_text(my_playbook)

    gather_roles = True
    testvars_roles_blocklist = []
    testvars_roles_exclusivelist = ['my_role_2']
    testvars_roles_includelist = []
    testvars_roles_playbooks = []

    moleculeenv = MoleculeEnv(med,
                              msd,
                              gather_roles,
                              testvars_roles_blocklist,
                              testvars_roles_exclusivelist,
                              testvars_roles_includelist,
                              testvars_roles_playbooks)

    assert moleculeenv.get_roles() == my_roles


def test_takeltest_unit_moleculeenv_get_roles_included(tmp_path):
    my_playbook = """\
---
- name: converge
  hosts: all
  gather_facts: false
  roles:
    - my_role_1
"""
    my_roles = ['my_role_1', 'my_role_2']

    med = tmp_path / 'molecule_ephemeral_directory'
    med.mkdir()

    msd = tmp_path / 'molecule_scenario_directory'
    msd.mkdir()

    my_role_1 = tmp_path / 'roles' / 'my_role_1'
    my_role_1.mkdir(parents=True)

    my_role_2 = tmp_path / 'roles' / 'my_role_2'
    my_role_2.mkdir()

    playbook_path = msd / 'playbook.yml'
    playbook_path.write_text(my_playbook)

    gather_roles = True
    testvars_roles_blocklist = []
    testvars_roles_exclusivelist = []
    testvars_roles_includelist = ['my_role_2']
    testvars_roles_playbooks = []

    moleculeenv = MoleculeEnv(med,
                              msd,
                              gather_roles,
                              testvars_roles_blocklist,
                              testvars_roles_exclusivelist,
                              testvars_roles_includelist,
                              testvars_roles_playbooks)

    assert moleculeenv.get_roles() == my_roles


def test_takeltest_unit_moleculeenv_get_roles_playbook(tmp_path):
    my_playbook = """\
---
- name: converge
  hosts: all
  gather_facts: false
  roles:
    - my_role_1
"""
    my_roles = ['my_role_1']

    med = tmp_path / 'molecule_ephemeral_directory'
    med.mkdir()

    msd = tmp_path / 'molecule_scenario_directory'
    msd.mkdir()

    my_role_1 = tmp_path / 'roles' / 'my_role_1'
    my_role_1.mkdir(parents=True)

    playbook_path = tmp_path / 'custom.yml'
    playbook_path.write_text(my_playbook)

    gather_roles = True
    testvars_roles_blocklist = []
    testvars_roles_exclusivelist = []
    testvars_roles_includelist = []
    testvars_roles_playbooks = ['../custom.yml']

    moleculeenv = MoleculeEnv(med,
                              msd,
                              gather_roles,
                              testvars_roles_blocklist,
                              testvars_roles_exclusivelist,
                              testvars_roles_includelist,
                              testvars_roles_playbooks)

    assert moleculeenv.get_roles() == my_roles


def test_takeltest_unit_moleculeenv_get_roles_playbooks(tmp_path):
    my_playbook_1 = """\
---
- name: converge
  hosts: all
  gather_facts: false
  roles:
    - my_role_1
"""
    my_playbook_2 = """\
---
- name: converge
  hosts: all
  gather_facts: false
  roles:
    - my_role_2
"""
    my_roles = ['my_role_1', 'my_role_2']

    med = tmp_path / 'molecule_ephemeral_directory'
    med.mkdir()

    msd = tmp_path / 'molecule_scenario_directory'
    msd.mkdir()

    my_role_1 = tmp_path / 'roles' / 'my_role_1'
    my_role_1.mkdir(parents=True)

    my_role_2 = tmp_path / 'roles' / 'my_role_2'
    my_role_2.mkdir(parents=True)

    playbook_path = tmp_path / 'custom1.yml'
    playbook_path.write_text(my_playbook_1)

    playbook_path = tmp_path / 'custom2.yml'
    playbook_path.write_text(my_playbook_2)

    gather_roles = True
    testvars_roles_blocklist = []
    testvars_roles_exclusivelist = []
    testvars_roles_includelist = []
    testvars_roles_playbooks = ['../custom1.yml', '../custom2.yml']

    moleculeenv = MoleculeEnv(med,
                              msd,
                              gather_roles,
                              testvars_roles_blocklist,
                              testvars_roles_exclusivelist,
                              testvars_roles_includelist,
                              testvars_roles_playbooks)

    assert moleculeenv.get_roles() == my_roles


def test_takeltest_unit_moleculeenv_get_roles_fallback_project(tmp_path):
    my_roles = ['my_role_1']

    med = tmp_path / 'molecule_ephemeral_directory'
    med.mkdir()

    msd = tmp_path / 'molecule/molecule_scenario_directory'
    msd.mkdir(parents=True)

    my_role_1 = tmp_path / 'roles' / 'my_role_1'
    my_role_1.mkdir(parents=True)

    gather_roles = True
    testvars_roles_blocklist = []
    testvars_roles_exclusivelist = []
    testvars_roles_includelist = []
    testvars_roles_playbooks = []

    moleculeenv = MoleculeEnv(med,
                              msd,
                              gather_roles,
                              testvars_roles_blocklist,
                              testvars_roles_exclusivelist,
                              testvars_roles_includelist,
                              testvars_roles_playbooks)

    assert moleculeenv.get_roles() == my_roles


def test_takeltest_unit_moleculeenv_get_roles_fallback_molecule(tmp_path):
    my_roles = ['my_role_1']

    med = tmp_path / 'molecule_ephemeral_directory'
    med.mkdir()

    msd = tmp_path / 'molecule/playbooks/roles' \
        / 'my_role_1/molecule/molecule_scenario_directory'
    msd.mkdir(parents=True)

    gather_roles = True
    testvars_roles_blocklist = []
    testvars_roles_exclusivelist = []
    testvars_roles_includelist = []
    testvars_roles_playbooks = []

    moleculeenv = MoleculeEnv(med,
                              msd,
                              gather_roles,
                              testvars_roles_blocklist,
                              testvars_roles_exclusivelist,
                              testvars_roles_includelist,
                              testvars_roles_playbooks)

    assert moleculeenv.get_roles() == my_roles


def test_takeltest_unit_moleculeenv_vars_config_molecule_yml(tmp_path):
    med = tmp_path / 'molecule_ephemeral_directory'
    med.mkdir()

    msd = tmp_path / 'molecule_scenario_directory'
    msd.mkdir()

    gather_roles = True
    testvars_roles_blocklist = []
    testvars_roles_exclusivelist = []
    testvars_roles_includelist = []
    testvars_roles_playbooks = []

    moleculeenv = MoleculeEnv(med,
                              msd,
                              gather_roles,
                              testvars_roles_blocklist,
                              testvars_roles_exclusivelist,
                              testvars_roles_includelist,
                              testvars_roles_playbooks)

    expected_config = 'Using variables defined in ' + str(msd / 'molecule.yml')
    molecule_vars_config = moleculeenv._get_molecule_vars_config_()
    assert molecule_vars_config == expected_config


def test_takeltest_unit_moleculeenv_vars_config_group_vars(tmp_path):
    med = tmp_path / 'molecule_ephemeral_directory'
    med.mkdir()

    msd = tmp_path / 'molecule_scenario_directory'
    msd.mkdir()

    group_vars_target = msd / 'group_vars'
    group_vars_target.mkdir()

    inventory_dir = med / 'inventory'
    inventory_dir.mkdir()

    group_vars = inventory_dir / 'group_vars'
    group_vars.symlink_to(group_vars_target, target_is_directory=True)

    gather_roles = True
    testvars_roles_blocklist = []
    testvars_roles_exclusivelist = []
    testvars_roles_includelist = []
    testvars_roles_playbooks = []

    moleculeenv = MoleculeEnv(med,
                              msd,
                              gather_roles,
                              testvars_roles_blocklist,
                              testvars_roles_exclusivelist,
                              testvars_roles_includelist,
                              testvars_roles_playbooks)

    expected_config = 'Using group_vars symlink to ' + str(group_vars_target)
    molecule_vars_config = moleculeenv._get_molecule_vars_config_()
    assert molecule_vars_config == expected_config


def test_takeltest_unit_moleculeenv_vars_config_host_vars(tmp_path):
    med = tmp_path / 'molecule_ephemeral_directory'
    med.mkdir()

    msd = tmp_path / 'molecule_scenario_directory'
    msd.mkdir()

    host_vars_target = msd / 'host_vars'
    host_vars_target.mkdir()

    inventory_dir = med / 'inventory'
    inventory_dir.mkdir()

    host_vars = inventory_dir / 'host_vars'
    host_vars.symlink_to(host_vars_target, target_is_directory=True)

    gather_roles = True
    testvars_roles_blocklist = []
    testvars_roles_exclusivelist = []
    testvars_roles_includelist = []
    testvars_roles_playbooks = []

    moleculeenv = MoleculeEnv(med,
                              msd,
                              gather_roles,
                              testvars_roles_blocklist,
                              testvars_roles_exclusivelist,
                              testvars_roles_includelist,
                              testvars_roles_playbooks)

    expected_config = 'Using host_vars symlink to ' + str(host_vars_target)
    molecule_vars_config = moleculeenv._get_molecule_vars_config_()
    assert molecule_vars_config == expected_config


def test_takeltest_unit_moleculeenv_vars_config_host_vars_and_group_vars(
        tmp_path):
    med = tmp_path / 'molecule_ephemeral_directory'
    med.mkdir()

    msd = tmp_path / 'molecule_scenario_directory'
    msd.mkdir()

    group_vars_target = msd / 'group_vars'
    group_vars_target.mkdir()

    host_vars_target = msd / 'host_vars'
    host_vars_target.mkdir()

    inventory_dir = med / 'inventory'
    inventory_dir.mkdir()

    group_vars = inventory_dir / 'group_vars'
    group_vars.symlink_to(group_vars_target, target_is_directory=True)

    host_vars = inventory_dir / 'host_vars'
    host_vars.symlink_to(host_vars_target, target_is_directory=True)

    gather_roles = True
    testvars_roles_blocklist = []
    testvars_roles_exclusivelist = []
    testvars_roles_includelist = []
    testvars_roles_playbooks = []

    moleculeenv = MoleculeEnv(med,
                              msd,
                              gather_roles,
                              testvars_roles_blocklist,
                              testvars_roles_exclusivelist,
                              testvars_roles_includelist,
                              testvars_roles_playbooks)

    expected_config = 'Using group_vars symlink to ' + str(group_vars_target)
    expected_config += '\n'
    expected_config += 'Using host_vars symlink to ' + str(host_vars_target)
    molecule_vars_config = moleculeenv._get_molecule_vars_config_()
    assert molecule_vars_config == expected_config
