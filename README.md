# takelage-var

*takelage-var* provides the [pytest](https://pytest.org/)
plugin [pytest-takeltest](https://pypi.org/project/pytest-takeltest/)
for the takelage devops workflow.
The takelage devops workflow helps devops engineers
build, test and deploy os images.

The pytest plugin 
[pytest-testinfra](https://testinfra.readthedocs.io/en/latest/)
allows to write unit tests in python to test
your servers configured by the management tool 
[ansible](https://www.ansible.com/).
testinfra is a
[verifier](https://molecule.readthedocs.io/en/stable/configuration.html#testinfra)
of the [molecule]( https://molecule.readthedocs.io/)
testing environment.

The pytest plugin pytest-takeltest provides helper functions
and fixtures to facilitate the use of molecule and testinfra.
It provides access to variables and secrets and helps to not only 
unit test your ansible roles but to
integration and system test your whole ansible project.

pytest-testinfra wraps 
[cli](https://philpep.org/blog/infrastructure-testing-with-testinfra) 
calls to the ansible executable.
pytest-takeltest uses the
[ansible runner](https://ansible.readthedocs.io/projects/runner/en/latest/)
to leverage the ansible python api and run playbooks.

## Framework Versions

| Project | Artifacts |
|-|-|
| [![takelage-doc](https://img.shields.io/badge/github-takelage--doc-purple)](https://github.com/takelwerk/takelage-doc) | [![License](https://img.shields.io/badge/license-GNU_GPLv3-blue)](https://github.com/takelwerk/takelage-doc/blob/main/LICENSE) |
| [![takelage-var](https://img.shields.io/badge/github-takelage--var-purple)](https://github.com/takelwerk/takelage-var) | [![pypi,org](https://img.shields.io/pypi/v/pytest-takeltest?label=pypi.org&color=blue)](https://pypi.org/project/pytest-takeltest/) |
| [![takelage-cli](https://img.shields.io/badge/github-takelage--cli-purple)](https://github.com/takelwerk/takelage-cli) | [![rubygems.org](https://img.shields.io/gem/v/takeltau?label=rubygems.org&color=blue)](https://rubygems.org/gems/takeltau) |
| [![takelage-img-takelslim](https://img.shields.io/badge/github-takelage--img--takelslim-purple)](https://github.com/takelwerk/takelage-img-takelslim) | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelslim/latest-amd64?label=hub.docker.com&arch=amd64&color=teal)](https://hub.docker.com/r/takelwerk/takelslim) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelslim/latest-arm64?label=hub.docker.com&arch=arm64&color=slateblue)](https://hub.docker.com/r/takelwerk/takelslim) | 
| [![takelage-img-takelbase](https://img.shields.io/badge/github-takelage--img--takelbase-purple)](https://github.com/takelwerk/takelage-img-takelbase) | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelbase/latest-amd64?label=hub.docker.com&arch=amd64&color=teal)](https://hub.docker.com/r/takelwerk/takelbase) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelbase/latest-arm64?label=hub.docker.com&arch=arm64&color=slateblue)](https://hub.docker.com/r/takelwerk/takelbase) |
| [![takelage-img-takelpodslim](https://img.shields.io/badge/github-takelage--img--takelpodslim-purple)](https://github.com/takelwerk/takelage-img-takelpodslim) | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpodslim/latest-amd64?label=hub.docker.com&arch=amd64&color=teal)](https://hub.docker.com/r/takelwerk/takelpodslim) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpodslim/latest-arm64?label=hub.docker.com&arch=arm64&color=slateblue)](https://hub.docker.com/r/takelwerk/takelpodslim) | 
| [![takelage-img-takelpodbase](https://img.shields.io/badge/github-takelage--img--takelpodbase-purple)](https://github.com/takelwerk/takelage-img-takelpodbase) | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpodbase/latest-amd64?label=hub.docker.com&arch=amd64&color=teal)](https://hub.docker.com/r/takelwerk/takelpodbase) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpodbase/latest-arm64?label=hub.docker.com&arch=arm64&color=slateblue)](https://hub.docker.com/r/takelwerk/takelpodbase) | 
| [![takelage-dev](https://img.shields.io/badge/github-takelage--dev-purple)](https://github.com/takelwerk/takelage-dev) | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelage/latest-amd64?label=hub.docker.com&arch=amd64&sort=semver&color=teal)](https://hub.docker.com/r/takelwerk/takelage) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelage/latest-arm64?label=hub.docker.com&arch=arm64&sort=semver&color=slateblue)](https://hub.docker.com/r/takelwerk/takelage) |
| [![takelage-pad](https://img.shields.io/badge/github-takelage--pad-purple)](https://github.com/takelwerk/takelage-pad) | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpad/latest-amd64?label=hub.docker.com&arch=amd64&sort=semver&color=teal)](https://hub.docker.com/r/takelwerk/takelpad) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpad/latest-arm64?label=hub.docker.com&arch=arm64&sort=semver&color=slateblue)](https://hub.docker.com/r/takelwerk/takelpad) |
| [![takelship](https://img.shields.io/badge/github-takelship-purple)](https://github.com/takelwerk/takelship) | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelship/latest-amd64?label=hub.docker.com&arch=amd64&sort=semver&color=teal)](https://hub.docker.com/r/takelwerk/takelship) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelship/latest-arm64?label=hub.docker.com&arch=arm64&sort=semver&color=slateblue)](https://hub.docker.com/r/takelwerk/takelship) | |


## Framework Status

| Project | Pipelines |
|-|-|
| [![takelage-var](https://img.shields.io/badge/github-takelage--var-purple)](https://github.com/takelwerk/takelage-var) | [![takeltest](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-var/takeltest.yml?label=takeltest)](https://github.com/takelwerk/takelage-var/actions/workflows/takeltest.yml) [![test_takeltest](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-var/test_takeltest.yml?label=test%20takeltest)](https://github.com/takelwerk/takelage-var/actions/workflows/test_takeltest.yml) |
| [![takelage-cli](https://img.shields.io/badge/github-takelage--cli-purple)](https://github.com/takelwerk/takelage-cli) | [![takeltau](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-cli/takeltau.yml?label=takeltau)](https://github.com/takelwerk/takelage-cli/actions/workflows/takeltau.yml) [![test_takeltau](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-cli/test_takeltau.yml?label=test%20takeltau)](https://github.com/takelwerk/takelage-cli/actions/workflows/test_takeltau.yml) |
| [![takelage-img-takelslim](https://img.shields.io/badge/github-takelage--img--takelslim-purple)](https://github.com/takelwerk/takelage-img-takelslim) | [![takelslim amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-img-takelslim/takelslim_amd64.yml?label=takelslim%20amd64)](https://github.com/takelwerk/takelage-img-takelslim/actions/workflows/takelslim_amd64.yml) |
| [![takelage-img-takelbase](https://img.shields.io/badge/github-takelage--img--takelbase-purple)](https://github.com/takelwerk/takelage-img-takelbase) | [![takelbase amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-img-takelbase/takelbase_amd64.yml?label=takelbase%20amd64)](https://github.com/takelwerk/takelage-img-takelbase/actions/workflows/takelbase_amd64.yml) | 
| [![takelage-img-takelpodslim](https://img.shields.io/badge/github-takelage--img--takelpodslim-purple)](https://github.com/takelwerk/takelage-img-takelpodslim) | [![takelpodslim amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-img-takelpodslim/takelpodslim_amd64.yml?label=takelpodslim%20amd64)](https://github.com/takelwerk/takelage-img-takelpodslim/actions/workflows/takelpodslim_amd64.yml) |
| [![takelage-img-takelpodbase](https://img.shields.io/badge/github-takelage--img--takelpodbase-purple)](https://github.com/takelwerk/takelage-img-takelpodbase) | [![takelpodbase amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-img-takelpodbase/takelpodbase_amd64.yml?label=takelpodbase%20amd64)](https://github.com/takelwerk/takelage-img-takelpodbase/actions/workflows/takelpodbase_amd64.yml) | 
| [![takelage-dev](https://img.shields.io/badge/github-takelage--dev-purple)](https://github.com/takelwerk/takelage-dev) | [![takelage amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/takelage_amd64.yml?label=takelage%20amd64)](https://github.com/takelwerk/takelage-dev/actions/workflows/takelage_amd64.yml) [![test_takelage](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/test_takelage.yml?label=test%20takelage)](https://github.com/takelwerk/takelage-dev/actions/workflows/test_takelage.yml) 
| | [![takelbuild amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/takelbuild_amd64.yml?label=takelbuild%20amd64)](https://github.com/takelwerk/takelage-dev/actions/workflows/takelbuild_amd64.yml) [![test_takelbuild](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/test_takelbuild.yml?label=test%20takelbuild)](https://github.com/takelwerk/takelage-dev/actions/workflows/test_takelbuild.yml) |
| | [![takelbeta amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/takelbeta_amd64.yml?label=takelbeta%20amd64)](https://github.com/takelwerk/takelage-dev/actions/workflows/takelbeta_amd64.yml) [![test_roles](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/test_roles.yml?label=test%20roles)](https://github.com/takelwerk/takelage-dev/actions/workflows/test_roles.yml) |
| [![takelage-pad](https://img.shields.io/badge/github-takelage--pad-purple)](https://github.com/takelwerk/takelage-pad) | [![takelpad docker](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-pad/takelpad_docker.yml?label=takelpad%20docker)](https://github.com/takelwerk/takelage-pad/actions/workflows/takelpad_docker.yml) |
| | [![test takelpad](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-pad/test_takelpad.yml?label=test%20takelpad)](https://github.com/takelwerk/takelage-pad/actions/workflows/test_takelpad.yml) [![test roles](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-pad/test_roles.yml?label=test%20roles)](https://github.com/takelwerk/takelage-pad/actions/workflows/test_roles.yml) |
| [![takelship](https://img.shields.io/badge/github-takelship-purple)](https://github.com/takelwerk/takelship) | [![takelship docker](https://img.shields.io/github/actions/workflow/status/takelwerk/takelship/takelship-amd64.yml?label=takelship%20docker)](https://github.com/takelwerk/takelship/actions/workflows/takelship-amd64.yml) |

## Installation

Install the pytest-takeltest pytest 
[plugin](https://pypi.org/project/pytest-takeltest/)
using [pip](https://packaging.python.org/tutorials/installing-packages/):

```bash
pip install pytest-takeltest
```

## Tests

Run pytest unit tests and molecule system tests by invoking
[rake](https://github.com/ruby/rake):

```bash
rake test
```

## Example

Have a look at 
[anarchism](test/system/anarchism) and
[env](test/system/env)
system test directories for examples
of molecule projects using ansible, pytest-testinfra and pytest-takeltest.

## Boilerplate

As a boilerplate for testinfra tests it is enough to do:

```python
import pytest-takeltest

testinfra_hosts = takeltest.hosts()
``` 

## Fixtures multitestvars and testvars

Arguably the most useful feature of the pytest-takeltest plugin
are the *multitestvars* and *testvars* fixtures.
The fixtures resolve and expose 
ansible variables as a python dict:

```python
def test_mytest(multitestvars):

    my_python_variable = multitestvars['my_host']['my_ansible_variable']
```

*testvars* is a list containing the ansible variables 
of the first molecule host. Use this if you only have one host:

```python
def test_mytest(testvars):

    my_python_variable = testvars['my_ansible_variable']
```

*multitestvars* runs a playbook against the molecule hosts 
using the ansible runner.

*multitestvars* creates a symbolic link to the roles directory of your 
ansible project in the ephemeral playbook environment which molecule sets up.
It then runs a playbook with ``gather_facts:true`` and a debug task 
to get the ansible variables and the ansible facts of the play and host.

*multitestvars* uses the ansible runner so the usual ansible variable 
[precedence rules](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable)
apply. Internally, the fixture uses the ansible
[debug module](https://docs.ansible.com/ansible/latest/modules/debug_module.html)
to resolve templates.
Thus, it can resolve any kind of template
which the debug module can resolve including
[jinja2](http://jinja.pocoo.org/) code and calls to 
[lookup plugins](https://docs.ansible.com/ansible/latest/plugins/lookup.html).

### extra vars

The ``TESTVARS_EXTRA_VARS`` environment variable can be set in ``molecule.yml``.
It can contain dirpaths or filepaths relative to the
``MOLECULE_SCENARIO_DIRECTORY`` separated by colons:

```yaml
verifier:
  name: testinfra
  env:
    TESTVARS_EXTRA_VARS: "../../vars:../../extra_vars/extra_vars.yml"
```

The vars files will be included in moleculebook playbooks by adding
the paths to ``vars_files`` (as opposed to adding ``include_vars`` tasks).

### roles

Which roles are included is determined in the following order,
the first match wins:

- List of roles separated by colon specified in the
  ``TESTVARS_ROLES_EXCLUSIVE`` environment variable.
- List of roles specified in playbooks separated by colon specified in 
  ``TESTVARS_ROLES_PLAYBOOKS`` environment variable.
- List of roles specified in playbook specified in 
  ``molecule.yml``
- List of roles specified in default playbook
  ``converge.yml``
- List of roles specified in old default playbook
  ``playbook.yml``
- All roles in ``roles`` directory in project directory

Roles included in ``TESTVARS_ROLES_INCLUDE`` will be included.
Roles blocked in ``TESTVARS_ROLES_BLOCK`` won't be included.

You may want to include roles which are 
[imported by task](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/import_role_module.html)
and not by playbook.

You can find the source code in the function ``_configure_roles_`` in
[moleculeenv.py](https://github.com/takelwerk/takelage-var/blob/master/takeltest/moleculeenv.py).

### example: testing packer images

By specifying playbooks via ``TESTVARS_ROLES_PLAYBOOKS``
you are able to test your packer images with molecule.
Let's assume your local docker image is called
``packer_local/my_image``. 
Then you can start this image within a molecule scenario:

```yaml
platforms:
- name: molecule-my-image
  image: packer_local/my_image
```

Make the group_vars (and host_vars, if you wish so) available to pytest-takeltest:

```yaml
provisioner:
  name: ansible
  inventory:
    links:
      group_vars: ../../group_vars/
```

Now you don't want to run your playbook on that packer image again.
But you still want to have access to all the role defaults variables
of those roles defined in your playbook so that your tests will pass.
Either you do not run ``molecule converge`` and ``molecule idempotence``
on your image or you set the ``TESTVARS_ROLES_PLAYBOOKS`` environment variable:

```yaml
verifier:
  name: testinfra
  env:
    TESTVARS_ROLES_PLAYBOOKS: ../../site.yml:../../my_layer.yml
```

Code examples are the
[takelbuild_converge scenario](test/system/anarchism/molecule/takelbuild_converge)
and the
[takelbuild_custom scenario](test/system/anarchism/molecule/takelbuild_custom)
of the anarchism project. 
Omitting ``molecule converge`` and ``molecule idempotence`` has the
advantage that your pytests are automagically included.

Both scenarios achieve the same but use different methods.
The takelbuild server happens to be built with the same role
[takel_anarchism](test/system/anarchism/roles/takel_anarchism)
whose unit tests are applied in these scenarios to the
[takelbuild server](https://github.com/takelwerk/takelage-dev)
docker image.

### options

*multitestvars* and *testvars* are session scope fixtures
so they are configured in
``molecule.yml`` by using pytest command line options.
You can add a couple of options in the options dictionary
of the verifier section:

```yaml
verifier:
  name: testinfra
  options:
    testvars-no-gather-facts: true
```

By default, *multitestvars* runs a playbook
to gather ansible variables and facts.
It then runs a playbook to resolve the variables.

You can change the default behaviour with these options:

- ``testvars-no-gather-facts``
    Run playbook to gather variables with ``gather_facts: false``.
    You won't be able to access ``ansible_facts``
    but your tests will run faster.
- ``testvars-no-gather-molecule``
    Do not resolve molecule variables.
    You probably won't need these variables
    but it won't take much time to resolve them, either.
- ``testvars-no-extra-vars``
    Do not add extra variables specified in ``TESTVARS_EXTRA_VARS``.
    Ignores the environment variable.

### caching

Hopefully the *multitestvars* fixture allows fast test-driven development.
It has `session` scope so variables are collected and resolved only once
per testrun as pytest caches the result.
If this is still too slow for you then you can enable the pytest 
[cache plugin](https://docs.pytest.org/en/latest/cache.html)
in ``molecule.yml``:

```yaml
verifier:
  name: testinfra
  options:
    p: cacheprovider
```

You should use the pytest-takeltest boilerplate code to be able to run pytest directly.
Otherwise testinfra will complain about missing environment variables.

Remember to clear the cache when you add or change an ansible variable::

```bash
pytest --cache-clear; molecule verify
```

The cache will use the molecule ephemeral directory as the cache key which
is unique for each molecule instance.
When using the boilerplate you can inspect the cache by running::

```bash
pytest --cache-show
```

## Ansible Python API via Ansible Runner

The pytest-takeltest plugin provides two main pytest fixtures:

- *multitestvars* – resolves and exposes ansible vars and facts 
    of all molecule hosts
- *testvars* – resolves and exposes ansible vars and facts 
    of one molecule host
- *moleculebook* – api to run playbooks against a molecule host

The *multitestvars* and *testvars* fixtures use the 
*moleculebook* fixture which uses the ansible runner. 
The *moleculeenv* fixture handles the sysadmin tasks of setting the right symlinks, creating and deleting files.
*moleculebook* might be handy in those situations where you know you
shouldn't implement a hackaround. ;-)

Here is how you could run an ansible playbook programmatically from 
a test (or even better: from a 
[fixture](https://docs.pytest.org/en/latest/fixture.html)) using dependency injection.

```python
def test_takeltest_moleculebook(host, moleculebook):
    playbook = moleculebook.get()
    task_touch = {
        'name': 'touch this file',
        'ansible.builtin.file': {
            'path': '/tmp/moleculebook_did_this',
            'state': 'touch'
        }
    }
    play = playbook[0]
    play['tasks'].append(task_touch)
    moleculebook.run([play])
    assert host.file('/tmp/moleculebook_did_this').exists
```

You can inspect the ansible logs in `~/.cache/molecule`.

See 
[takel-gem](https://github.com/takelwerk/takelage-dev/blob/main/ansible/roles/takel_gem/molecule/default/system/test_takel_gem_system.py)
for a real-world example in which moleculebook is used 
to avoid a molecule ``prepare.yml`` playbook
which otherwise needs to be copied 
to the project's molecule default scenario.
