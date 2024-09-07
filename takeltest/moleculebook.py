import ansible_runner


class MoleculeBook(object):
    '''Run an ansible playbook against a molecule host'''

    def __init__(self,
                 testvars_extra_vars,
                 moleculeinventory,
                 moleculeenv):
        self._hosts = moleculeinventory.hosts()
        self._moleculeenv = moleculeenv
        self._testvars_extra_vars = testvars_extra_vars
        self._playbook = dict()
        self.create()

    def get(self):
        '''Get the ansible playbook'''
        return self._playbook

    def set(self, playbook):
        '''Set an ansible playbook'''
        self._playbook = playbook

    def get_molecule_scenario_directory(self):
        return self._moleculeenv.get_molecule_scenario_directory()

    def get_roles(self):
        return self._moleculeenv.get_roles()

    def create(self,
               gather_facts=False,
               gather_roles=True,
               extra_vars=True,
               host=None):
        '''Create an ansible playbook using the ansible python api.'''
        if host is None:
            host = next(iter(self._hosts))

        play = dict(
            name="ansible playbook",
            hosts=host,
            gather_facts=str(gather_facts),
            vars_files=list(),
            roles=list(),
            tasks=list(),
        )
        playbook = [play]

        # include extra vars files
        if extra_vars:
            for path in self._get_extra_vars_():
                playbook[0]['vars_files'].append(str(path))

        # include roles
        if gather_roles:
            for role in self.get_roles():
                playbook[0]['roles'].append({'name': role, 'when': 'False'})
        self._playbook = playbook

    def add_task_debug_msg(self, msg, playbook, name='Debug'):
        '''Add a task using the ansible debug module'''
        task = {'name': name,
                'ansible.builtin.debug': {'msg': msg}}
        playbook[0]['tasks'].append(task)
        return playbook

    def add_task_get_vars(self, playbook, name='Get vars'):
        '''Add a task using the ansible debug module to gather variables'''
        msg = "{{ vars }}"
        task = {'name': name,
                'ansible.builtin.debug': {
                    'msg': msg}}
        playbook[0]['tasks'].append(task)
        return playbook

    def add_task_include_vars_dir(
            self,
            vars_dir,
            playbook,
            name='Include vars'):
        '''Add a task using the ansible include_vars module'''
        task = {'name': name,
                'ansible.builtin.include_vars': {
                    'dir': vars_dir}}
        playbook[0]['tasks'].append(task)
        return playbook

    def get_vars(
            self,
            host=None):
        '''Return ansible facts and vars of a molecule host.

        Args:
            gather_facts (bool): gather ansible_facts from a molecule host?
                Defaults to True.
                A playbook will be run with ``gather_facts:true``.
            extra_vars (bool): include extra vars from vars files?
                Defaults to True.
                An include_vars task will be added to include extra vars files
                specified in the environment variable TESTVARS_EXTRA_VARS
            host (string)

        Returns:
            dict: resolved ansible variables and facts
        '''

        playbook = self._playbook
        playbook[0]['hosts'] = host
        playbook[0]['gather_facts'] = True
        task_name = 'moleculebook_get_vars'

        # make sure that the variables from the last run
        # do not interfere with the next run
        self._moleculeenv.remove_extravars()

        # this is where the magic happens:
        # calling the debug module this way yields all variables
        self.add_task_get_vars(playbook, task_name)

        runner = self.run(playbook)
        vars = self._get_vars_from_event_data(runner, host, task_name)

        # some (role) variables may not be resolved yet
        # so we write all vars to env/extravars
        # (where they do get resolved)
        # and run ansible again
        self._moleculeenv.write_extravars(vars)
        runner = self.run(playbook)
        vars = self._get_vars_from_event_data(runner, host, task_name)

        # we write the resolved vars to disk again
        # you can inspect them at ~|.cache/molecule/.../env/extravars
        self._moleculeenv.write_extravars(vars)

        return vars

    def run(self, playbook):
        '''Run the ansible playbook'''
        self._moleculeenv.write_playbook(playbook)
        private_data_dir = self._moleculeenv.get_molecule_ephemeral_directory()
        r = ansible_runner.run(
            private_data_dir=private_data_dir,
            playbook='site.json',
            quiet=True)
        return r

    def _get_extra_vars_(self):
        return self._testvars_extra_vars

    def _get_molecule_scenario_directory_(self):
        return self._get_molecule_scenario_directory()

    def _get_vars_from_event_data(self, runner, host, task_name):
        for event in runner.events:
            try:
                if event['event'] == 'runner_on_ok':
                    if event['event_data']['task'] == task_name:
                        # Merge and overwrite all variables
                        # (some still unresolved)
                        # with the (resolved) hostvars
                        return (
                            event['event_data']['res']['msg'] |
                            event['event_data']['res']['msg']['hostvars'][host]
                        )
            except (IndexError, KeyError):
                continue
        return dict()
