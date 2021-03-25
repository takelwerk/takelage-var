import os
from pathlib import Path
import pytest
from takeltest.ansibleres import AnsibleInventory
from takeltest.moleculeenv import MoleculeEnv
from takeltest.moleculelog import MoleculeLog
from takeltest.moleculeplay import MoleculePlay
from takeltest.moleculebook import MoleculeBook
from takeltest.multitestvars import MultiTestVars
from takeltest.templates import Templates
from takeltest.jsonvars import JsonVars
from takeltest.pathlist import PathList
from takeltest.testpass import TestPass


###########################################################
# global cleanup function
###########################################################


@pytest.fixture(scope="session", autouse=True)
def cleanup(request, moleculelog):
    if request.config.getoption("--debug"):
        request.addfinalizer(moleculelog.print_debug)


###########################################################
# command line options: testvars group
###########################################################


def pytest_addoption(parser):
    parser.addini('log', 'test')
    testvars_optiongroup = parser.getgroup("testvars")
    testvars_optiongroup.addoption(
        "--testvars-debug-jsonvars",
        action="store_true",
        default=False,
        help="print jsonvars debug information")
    testvars_optiongroup.addoption(
        "--testvars-no-gather-facts",
        action="store_false",
        default=True,
        help="do not gather ansible_facts")
    testvars_optiongroup.addoption(
        "--testvars-no-gather-molecule",
        action="store_false",
        default=True,
        help="do not resolve molecule vars")
    testvars_optiongroup.addoption(
        "--testvars-no-gather-roles",
        action="store_false",
        default=True,
        help="do not gather vars from roles")
    testvars_optiongroup.addoption(
        "--testvars-no-extra-vars",
        action="store_false",
        default=True,
        help="do not include extra vars")


###########################################################
# fixtures: testvars option booleans
###########################################################


@pytest.fixture(scope='session')
def debug_jsonvars(request):
    '''testvars option --testvars-debug-jsonvars'''
    return request.config.getoption("--testvars-debug-jsonvars")


@pytest.fixture(scope='session')
def gather_facts(request):
    '''testvars option --testvars-no-gather-facts'''
    return request.config.getoption("--testvars-no-gather-facts")


@pytest.fixture(scope='session')
def gather_molecule(request):
    '''testvars option --testvars-no-gather-molecule'''
    return request.config.getoption("--testvars-no-gather-molecule")


@pytest.fixture(scope='session')
def gather_roles(request):
    '''testvars option --testvars-no-gather-roles'''
    return request.config.getoption("--testvars-no-gather-roles")


@pytest.fixture(scope='session')
def extra_vars(request):
    '''testvars option --testvars-no-extra-vars'''
    return request.config.getoption("--testvars-no-extra-vars")


###########################################################
# fixtures: testvars option lists
###########################################################


@pytest.fixture(scope='session')
def testvars_roles_blocklist(molecule_scenario_directory):
    '''environment variable TESTVARS_ROLES_BLOCK'''
    try:
        blocklist = os.environ['TESTVARS_ROLES_BLOCK']
    except KeyError:
        return list()
    return blocklist.split(':')


@pytest.fixture(scope='session')
def testvars_roles_exclusivelist(molecule_scenario_directory):
    '''environment variable TESTVARS_ROLES_EXCLUSIVE'''
    try:
        exclusivelist = os.environ['TESTVARS_ROLES_EXCLUSIVE']
    except KeyError:
        return list()
    return exclusivelist.split(':')


@pytest.fixture(scope='session')
def testvars_roles_includelist(molecule_scenario_directory):
    '''environment variable TESTVARS_ROLES_INCLUDE'''
    try:
        includelist = os.environ['TESTVARS_ROLES_INCLUDE']
    except KeyError:
        return list()
    return includelist.split(':')


@pytest.fixture(scope='session')
def testvars_roles_playbooks(molecule_scenario_directory):
    '''environment variable TESTVARS_ROLES_PLAYBOOKS'''
    try:
        playbooks = os.environ['TESTVARS_ROLES_PLAYBOOKS']
    except KeyError:
        return None
    return playbooks.split(':')


@pytest.fixture(scope='session')
def testvars_extra_vars(molecule_scenario_directory):
    '''environment variable TESTVARS_EXTRA_VARS'''
    try:
        extra_vars = Path(os.environ['TESTVARS_EXTRA_VARS'])
    except KeyError:
        return list()
    return PathList(
        extra_vars,
        molecule_scenario_directory).get()


###########################################################
# fixtures: ansible resources
###########################################################


@pytest.fixture(scope='session')
def ansibleinventory(inventory_file):
    return AnsibleInventory(
        inventory_file).get()


###########################################################
# fixtures: molecule resources
###########################################################


@pytest.fixture(scope='session')
def moleculelog():
    return MoleculeLog()


@pytest.fixture(scope='session')
def molecule_ephemeral_directory(tmp_path_factory):
    '''environment variable MOLECULE_EPHEMERAL_DIRECTORY'''
    try:
        dir = Path(os.environ['MOLECULE_EPHEMERAL_DIRECTORY'])
    except KeyError:
        dir = tmp_path_factory.mktemp('molecule_ephemeral_directory')
    return dir


@pytest.fixture(scope='session')
def molecule_scenario_directory(tmp_path_factory):
    '''environment variable MOLECULE_SCENARIO_DIRECTORY'''
    try:
        dir = Path(os.environ['MOLECULE_SCENARIO_DIRECTORY'])
    except KeyError:
        dir = tmp_path_factory.mktemp('molecule_scenario_directory')
    return dir


@pytest.fixture(scope='session')
def inventory_file(molecule_ephemeral_directory):
    '''Molecule managed ansible inventory file.'''
    inventory_file = molecule_ephemeral_directory / \
        'inventory/ansible_inventory.yml'
    inventory_dir = molecule_ephemeral_directory / 'inventory'
    inventory_dir.mkdir(exist_ok=True)
    if not inventory_file.is_file():
        inventory = "localhost"
        inventory_file.write_text(inventory)
    return inventory_file


@pytest.fixture(scope='session')
def moleculeenv(
        moleculelog,
        molecule_ephemeral_directory,
        molecule_scenario_directory,
        gather_roles,
        testvars_roles_blocklist,
        testvars_roles_exclusivelist,
        testvars_roles_includelist,
        testvars_roles_playbooks):
    return MoleculeEnv(
        moleculelog,
        molecule_ephemeral_directory,
        molecule_scenario_directory,
        gather_roles,
        testvars_roles_blocklist,
        testvars_roles_exclusivelist,
        testvars_roles_includelist,
        testvars_roles_playbooks)


###########################################################
# fixtures: ansible python api
###########################################################


@pytest.fixture(scope='session')
def moleculeplay(
        ansibleinventory,
        moleculeenv):
    '''Expose ansible python api to run playbooks against a molecule host.'''
    return MoleculePlay(
        ansibleinventory,
        moleculeenv)


@pytest.fixture(scope='session')
def moleculebook(
        testvars_extra_vars,
        ansibleinventory,
        moleculeplay):
    '''Run an ansible playbook against a molecule host.'''
    return MoleculeBook(
        testvars_extra_vars,
        ansibleinventory,
        moleculeplay)


###########################################################
# fixtures: testvars helpers
###########################################################


@pytest.fixture(scope='session')
def templates(moleculebook):
    return Templates(moleculebook)


@pytest.fixture(scope='session')
def jsonvars(
        templates,
        gather_molecule):
    return JsonVars(
        templates,
        gather_molecule)


@pytest.fixture(scope='session')
def cache_key(molecule_ephemeral_directory):
    # molecule_ephemeral_directory should be unique for each scenario
    return 'multitestvars' + str(molecule_ephemeral_directory)


###########################################################
# fixtures: molecule/testinfra/ansible helpers
###########################################################


@pytest.fixture(scope='session')
def testpass(moleculebook):
    '''Provide access to the ansible passwordstore lookup plugin.'''
    return TestPass(moleculebook).testpass


@pytest.fixture(scope='session')
def multitestvars(
        request,
        ansibleinventory,
        moleculelog,
        debug_jsonvars,
        moleculebook,
        jsonvars,
        gather_facts,
        extra_vars,
        cache_key):
    '''Expose ansible variables and facts of a molecule test scenario.'''
    multitestvars = MultiTestVars.get_cache(request, cache_key)
    if multitestvars is None:
        multitestvars_object = MultiTestVars(
            ansibleinventory,
            moleculelog,
            debug_jsonvars,
            moleculebook,
            jsonvars,
            gather_facts,
            extra_vars)
        multitestvars = multitestvars_object.get_multitestvars()
        multitestvars_object.set_cache(request, cache_key)
    return multitestvars


@pytest.fixture(scope='session')
def testvars(multitestvars):
    '''Expose ansible variables and facts of a molecule test scenario.'''
    return multitestvars[next(iter(multitestvars))]
