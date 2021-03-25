from pathlib import Path
from ruamel.yaml import YAML
from ruamel.yaml.scanner import ScannerError
import subprocess


class MoleculeEnv(object):

    def __init__(
            self,
            moleculelog,
            molecule_ephemeral_directory,
            molecule_scenario_directory,
            gather_roles,
            testvars_roles_blocklist,
            testvars_roles_exclusivelist,
            testvars_roles_includelist,
            testvars_roles_playbooks):
        self._molecule_ephemeral_directory = molecule_ephemeral_directory
        self._molecule_scenario_directory = molecule_scenario_directory
        self._gather_roles = gather_roles
        self._testvars_roles_blocklist = testvars_roles_blocklist
        self._testvars_roles_exclusivelist = testvars_roles_exclusivelist
        self._testvars_roles_includelist = testvars_roles_includelist
        self._testvars_roles_playbooks = testvars_roles_playbooks
        self._configure_roles_()
        self._moleculelog = moleculelog
        self._moleculelog.debug(self._get_molecule_vars_config_())
        self._moleculelog.debug('Using roles: ' + ','.join(self.get_roles()))

    def get_molecule_ephemeral_directory(self):
        return self._molecule_ephemeral_directory

    def get_molecule_scenario_directory(self):
        return self._molecule_scenario_directory

    def get_project_dir(self):
        '''Return ansible project dir.'''

        # start the ansible scenario directory
        path = self.get_molecule_scenario_directory()

        # go up until you find the roles dir
        while path != Path('/'):
            path = path.parent
            if path / 'roles' in [d for d in path.iterdir() if d.is_dir()]:
                return path

        # else return None
        return None

    def get_roles(self):
        '''Return roles as list of pathlib.Path objects'''
        roles_dir = self.get_molecule_ephemeral_directory() / 'roles'

        if not roles_dir.exists():
            return list()

        roles = sorted([d.name for d in roles_dir.iterdir() if d.is_dir()])
        return roles

    def _configure_roles_(self):
        '''Create symlinks to roles'''
        if self._gather_roles is False:
            return

        roles = None

        # exclusivelist selects roles directly
        if self._get_testvars_roles_exclusivelist_():
            roles = self._get_testvars_roles_exclusivelist_()

        # try to read roles from custom playbooks
        if roles is None:
            playbook_files = self._get_testvars_roles_playbooks_()
            if playbook_files is not None:
                for playbook_file in playbook_files:
                    if roles is None:
                        roles = []
                    roles += self._read_roles_from_playbook_(playbook_file)

        # try to read roles from custom molecule converge playbook
        if roles is None:
            playbook_file = self._read_playbook_file_from_molecule_yml_()
            if playbook_file is not None:
                roles = self._read_roles_from_playbook_(playbook_file)

        # try to read roles from default molecule 3 converge playbook
        if roles is None:
            roles = self._read_roles_from_playbook_('converge.yml')

        # try to read roles from default molecule 2 converge playbook
        if roles is None:
            roles = self._read_roles_from_playbook_('playbook.yml')

        # fallback: select all roles
        if roles is None:
            msd = self.get_molecule_scenario_directory()

            # roles dir viewed from a project molecule scenario
            roles_dir = msd / '../../roles'
            if roles_dir.is_dir():
                roles = sorted([d.name for d in roles_dir.iterdir()
                                if d.is_dir()])
            else:
                # roles dir viewed from a role molecule scenario
                roles_dir = msd / '../../../../roles'
                if roles_dir.is_dir():
                    roles = sorted([d.name for d in roles_dir.iterdir()
                                    if d.is_dir()])

        # apply include
        # by now, roles is a list
        roles = self._roles_apply_includelist_(roles)

        # if roles have been selected
        # then apply blocklist
        # then create symlinks
        # then return
        if roles is not None:
            roles = self._roles_apply_blocklist_(roles)
            self._create_roles_symlinks_(roles)
            return

    def _create_roles_symlinks_(self, roles):
        (self.get_molecule_ephemeral_directory() / 'roles').mkdir(
            exist_ok=True)
        for role in roles:
            self._create_symlink_('roles/' + role)

    def _create_symlink_(self, path):
        '''Create symlink from molecule ephemeral dir to project dir.'''
        project_dir = self.get_project_dir()
        if project_dir is None:
            return
        source = project_dir / path
        target = self.get_molecule_ephemeral_directory() / path
        try:
            target.symlink_to(source)
        except FileExistsError:
            pass

    def _get_molecule_vars_config_(self):
        molecule_vars_config = ''
        vars_config = list()

        group_vars = \
            self._molecule_ephemeral_directory / 'inventory/group_vars'
        host_vars = \
            self._molecule_ephemeral_directory / 'inventory/host_vars'

        if group_vars.is_symlink():
            target = self._molecule_scenario_directory / 'group_vars'
            vars_config.append('Using group_vars symlink to ' + str(target))

        if host_vars.is_symlink():
            target = self._molecule_scenario_directory / 'host_vars'
            vars_config.append('Using host_vars symlink to ' + str(target))

        if vars_config:
            molecule_vars_config = '\n'.join(vars_config)

            return molecule_vars_config

        # else no vars_config so we use the variables defined in molecule.yml
        molecule_yml = self._molecule_scenario_directory / 'molecule.yml'
        molecule_vars_config += \
            'Using variables defined in ' + str(molecule_yml)

        return molecule_vars_config

    def _get_testvars_roles_blocklist_(self):
        return self._testvars_roles_blocklist

    def _get_testvars_roles_exclusivelist_(self):
        return self._testvars_roles_exclusivelist

    def _get_testvars_roles_includelist_(self):
        return self._testvars_roles_includelist

    def _get_testvars_roles_playbooks_(self):
        return self._testvars_roles_playbooks

    def _read_playbook_file_from_molecule_yml_(self):
        molecule_yml_path = self.get_molecule_scenario_directory() / \
                            'molecule.yml'
        yaml = YAML(typ='safe')
        try:
            molecule_yml = yaml.load(molecule_yml_path)
            playbook_file = \
                molecule_yml['provisioner']['playbooks']['converge']
            command = [
                'bash',
                '-c',
                f"echo {playbook_file}"
            ]
            result = subprocess.run(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE).stdout.decode('UTF-8').strip()
            playbook_file = Path(result)
            return playbook_file
        except (FileNotFoundError, ScannerError, KeyError):
            return None

    def _read_roles_from_playbook_(self, playbook_file):
        playbook_path = self.get_molecule_scenario_directory() / playbook_file
        if not playbook_path.is_file():
            return None

        yaml = YAML(typ='safe')
        try:
            playbook = yaml.load(playbook_path)
            roles = playbook[0]['roles']
        except (FileNotFoundError, ScannerError, KeyError):
            return None

        # Roles are either a dict with string val, or string
        # this normalises them to list of strings
        roles = [r['role'] if isinstance(r, dict) else r for r in roles]

        return roles

    def _roles_apply_blocklist_(self, roles):
        roles_not_blocklisted = list()
        for role in roles:
            if role not in self._get_testvars_roles_blocklist_():
                roles_not_blocklisted.append(role)
        return roles_not_blocklisted

    def _roles_apply_includelist_(self, roles):
        roles_include = self._get_testvars_roles_includelist_()
        for role in roles_include:
            if role not in roles:
                roles.append(role)
        return roles
