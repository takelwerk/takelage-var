class MoleculeBook(object):
    '''Run an ansible playbook against a molecule host'''

    def __init__(self,
                 testvars_extra_vars,
                 moleculeinventory,
                 moleculeplay):
        self._hosts = moleculeinventory.hosts()
        self._moleculeplay = moleculeplay
        self._testvars_extra_vars = testvars_extra_vars
        self._playbook = dict()
        self.create()

    def get(self):
        '''Get the ansible playbook'''
        return self._playbook

    def set(self, playbook):
        '''Set an ansible playbook'''
        self._playbook = playbook

    def create(self,
               gather_facts=True,
               gather_roles=True,
               extra_vars=True,
               host=None):
        '''Create an ansible playbook using the ansible python api.'''
        if host is None:
            host = next(iter(self._hosts))

        playbook = dict(
            name="ansible playbook",
            hosts=host,
            gather_facts=str(gather_facts),
            vars_files=list(),
            roles=list(),
            tasks=list(),
        )

        # include extra vars files
        if extra_vars:
            for path in self._get_extra_vars_():
                playbook['vars_files'].append(str(path))

        # include roles
        if gather_roles:
            for role in self._moleculeplay.get_roles():
                playbook['roles'].append(dict(name=role, when='False'))

        self._playbook = playbook

    def add_task_debug_msg(self, msg):
        '''Add a task using the ansible debug module'''
        task = dict(action=dict(module='ansible.builtin.debug', args=dict(msg=msg)))
        self._playbook['tasks'].append(task)

    def first_task_debug_var(self, var):
        '''Add a first task using the ansible debug module'''
        task = dict(action=dict(module='ansible.builtin.debug', args=dict(var=var)))
        self._playbook['tasks'].insert(0, task)

    def add_task_include_vars_dir(self, vars_dir):
        '''Add a task using the ansible include_vars module'''
        args = dict(dir=str(vars_dir))
        task = dict(action=dict(module='include_vars', args=args))
        self._playbook['tasks'].append(task)

    def get_vars(
            self,
            gather_facts=True,
            extra_vars=True,
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
            vars (dict): resolved ansible variables and facts
        '''
        vars = dict()

        if not self._playbook:
            self.create(
                gather_facts=gather_facts,
                extra_vars=extra_vars,
                host=host)

        # this is where the magic happens:
        # calling the debug module this way yields all variables
        self.first_task_debug_var('{{ vars }}')

        runner = self.run()

        for event in runner.events:
            try:
                return event['event_data']['res']["<class 'dict'>"]
            except (IndexError, KeyError):
                continue

    def run(self):
        '''Run the ansible playbook'''
        return self._moleculeplay.run_playbook(self._playbook)

    def _get_extra_vars_(self):
        return self._testvars_extra_vars

    def _get_molecule_scenario_directory_(self):
        return self._moleculeplay.get_molecule_scenario_directory()
