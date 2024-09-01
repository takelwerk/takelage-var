import ansible_runner

class MoleculePlay(object):
    '''Run ansible playbooks against molecule host using the ansible runner.
    '''

    def __init__(
            self,
            moleculeenv):
        self._moleculeenv = moleculeenv

    def get_molecule_scenario_directory(self):
        return self._moleculeenv.get_molecule_scenario_directory()

    def get_roles(self):
        return self._moleculeenv.get_roles()

    def run_playbook(self, playbook):
        '''Run an ansible playbook using the ansible runner.'''
        private_data_dir = self._moleculeenv.get_molecule_scenario_directory()
        r = ansible_runner.run(
            private_data_dir=private_data_dir,
            playbook=playbook)
        return r
