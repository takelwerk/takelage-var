from ansible import context
from ansible.module_utils.common.collections import ImmutableDict
from ansible.parsing.dataloader import DataLoader
from ansible.playbook.play import Play
from ansible.vars.manager import VariableManager
from takeltest.ansiblerun import AnsibleRun
from ansible.parsing.vault import PromptVaultSecret, get_file_vault_secret
import os

class MoleculePlay(object):
    '''Run ansible playbooks against molecule host using the ansible python api.
    '''

    def __init__(
            self,
            ansibleinventory,
            moleculeenv):
        # Leverage the ansible python api
        # to run a playbook against a molecule host.
        #
        # see: ansible python api
        # https://docs.ansible.com/ansible/latest/dev_guide/developing_api.html

        self._moleculeenv = moleculeenv

        context.CLIARGS = ImmutableDict(
            connection='local',
            module_path=[''],
            forks=10,
            become=None,
            become_method=None,
            become_user=None,
            check=False,
            diff=False)
        loader = DataLoader()
        # Load ansible vault secrets
        vault_password_file = os.getenv('ANSIBLE_VAULT_PASSWORD_FILE')
        if vault_password_file :
            vault_id_name = 'default'
            file_vault_secret = get_file_vault_secret(filename=vault_password_file,vault_id=vault_id_name,loader=loader)
            file_vault_secret.load()
            loader.set_vault_secrets([(vault_password_file,file_vault_secret)])

        self._loader = loader
        self._inventory = ansibleinventory
        self._variable_manager = VariableManager(
            loader=loader,
            inventory=ansibleinventory)

    def get_molecule_scenario_directory(self):
        return self._moleculeenv.get_molecule_scenario_directory()

    def get_roles(self):
        return self._moleculeenv.get_roles()

    def run_playbook(self, playbook):
        '''Run an ansible playbook using the ansible python api.'''
        play = self._get_play_(playbook)
        ansiblerun = AnsibleRun(
            self._inventory,
            self._variable_manager,
            self._loader)
        result = ansiblerun.run(play)
        return result

    def _get_play_(self, playbook):
        return Play().load(
            playbook,
            variable_manager=self._variable_manager,
            loader=self._loader)
