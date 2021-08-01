[![license](https://img.shields.io/github/license/takelwerk/takelage-var?color=blueviolet)](https://github.com/takelwerk/takelage-var/blob/main/LICENSE)
[![pypi,org](https://img.shields.io/pypi/v/pytest-takeltest?label=pypi.org&color=blue)](https://pypi.org/project/pytest-takeltest/)
[![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-var/Build,%20test%20and%20deploy%20project?label=deploy%20project)](https://github.com/takelwerk/takelage-var/actions/workflows/build_test_deploy_project_on_push.yml)
[![test project](https://img.shields.io/github/workflow/status/takelwerk/takelage-var/Build%20and%20test%20project?label=test%20project)](https://github.com/takelwerk/takelage-var/actions/workflows/build_test_project_nightly.yml)

# takelage-var

*takelage-var* provides the [pytest](https://pytest.org/)
plugin [python-takeltest](https://pypi.org/project/pytest-takeltest/)
for the takelage devops workflow.
The takelage devops workflow helps devops engineers
build, test and deploy os images.

The pytest plugin 
[testinfra](https://testinfra.readthedocs.io/en/latest/)
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

testinfra wraps 
[cli](https://philpep.org/blog/infrastructure-testing-with-testinfra) 
calls to the ansible executable.
pytest-takeltest uses the ansible python
[api](https://docs.ansible.com/ansible/latest/dev_guide/developing_api.html)
to run ansible playbooks.

## Framework Versions

| App | Artifact |
| --- | -------- |
| *[takelage-doc](https://github.com/takelwerk/takelage-doc)* | [![License](https://img.shields.io/github/license/takelwerk/takelage-doc?color=blueviolet)](https://github.com/takelwerk/takelage-doc/blob/main/LICENSE) |
| *[takelage-dev](https://github.com/takelwerk/takelage-dev)* | [![hub.docker.com](https://img.shields.io/docker/v/takelage/takelage/latest?label=hub.docker.com&sort=semver&color=blue)](https://hub.docker.com/r/takelage/takelage) |
| *[takelage-cli](https://github.com/takelwerk/takelage-cli)* | [![rubygems.org](https://img.shields.io/gem/v/takelage?label=rubygems.org&color=blue)](https://rubygems.org/gems/takelage) |
| *[takelage-var](https://github.com/takelwerk/takelage-var)* | [![pypi,org](https://img.shields.io/pypi/v/pytest-takeltest?label=pypi.org&color=blue)](https://pypi.org/project/pytest-takeltest/) |
| *[takelage-bit](https://github.com/takelwerk/takelage-bit)* | [![hub.docker.com](https://img.shields.io/docker/v/takelage/bitboard/latest?label=hub.docker.com&sort=semver&color=blue)](https://hub.docker.com/r/takelage/bitboard) | 
| *[takelage-img-takelslim](https://github.com/takelwerk/takelage-img-takelslim)* | [![hub.docker.com](https://img.shields.io/docker/v/takelage/takelslim/latest?label=hub.docker.com&color=blue)](https://hub.docker.com/r/takelage/takelslim) | 
| *[takelage-img-takelbase](https://github.com/takelwerk/takelage-img-takelbase)* | [![hub.docker.com](https://img.shields.io/docker/v/takelage/takelbase/latest?label=hub.docker.com&color=blue)](https://hub.docker.com/r/takelage/takelbase) | 

## Framework Status

| App | Deploy project | Test project | Test roles |
| --- | -------------- | ------------ | ---------- |
| *[takelage-dev](https://github.com/takelwerk/takelage-dev)* | [![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-dev/Build,%20test%20and%20deploy%20project?label=deploy%20project)](https://github.com/takelwerk/takelage-dev/actions/workflows/build_test_deploy_project_on_push.yml) | [![test project](https://img.shields.io/github/workflow/status/takelwerk/takelage-dev/Build%20and%20test%20project?label=test%20project)](https://github.com/takelwerk/takelage-dev/actions/workflows/build_test_project_nightly.yml) | [![test roles](https://img.shields.io/github/workflow/status/takelwerk/takelage-dev/Test%20roles?label=test%20roles)](https://github.com/takelwerk/takelage-dev/actions/workflows/build_test_roles_nightly.yml) |
| *[takelage-cli](https://github.com/takelwerk/takelage-cli)* | [![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-cli/Build,%20test%20and%20deploy%20project?label=deploy%20project)](https://github.com/takelwerk/takelage-cli/actions/workflows/build_test_deploy_project_on_push.yml) | [![test project](https://img.shields.io/github/workflow/status/takelwerk/takelage-cli/Test%20project?label=test%20project)](https://github.com/takelwerk/takelage-cli/actions/workflows/test_project_nightly.yml) |
| *[takelage-var](https://github.com/takelwerk/takelage-var)* | [![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-var/Build,%20test%20and%20deploy%20project?label=deploy%20project)](https://github.com/takelwerk/takelage-var/actions/workflows/build_test_deploy_project_on_push.yml) | [![test project](https://img.shields.io/github/workflow/status/takelwerk/takelage-var/Build%20and%20test%20project?label=test%20project)](https://github.com/takelwerk/takelage-var/actions/workflows/build_test_project_nightly.yml) |
| *[takelage-bit](https://github.com/takelwerk/takelage-bit)* | [![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-bit/Build,%20test%20and%20deploy%20project?label=deploy%20project)](https://github.com/takelwerk/takelage-bit/actions/workflows/build_test_deploy_project_on_push.yml) | [![test project](https://img.shields.io/github/workflow/status/takelwerk/takelage-bit/Build%20and%20test%20project?label=test%20project)](https://github.com/takelwerk/takelage-bit/actions/workflows/build_test_project_nightly.yml) | [![test roles](https://img.shields.io/github/workflow/status/takelwerk/takelage-bit/Test%20roles?label=test%20roles)](https://github.com/takelwerk/takelage-bit/actions/workflows/build_test_roles_nightly.yml) |
| *[takelage-img-takelslim](https://github.com/takelwerk/takelage-img-takelslim)* | [![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-img-takelslim/Build%20and%20deploy%20takelslim?label=deploy%20project)](https://github.com/takelwerk/takelage-img-takelslim/actions/workflows/build_deploy_takelslim_nightly.yml) |
| *[takelage-img-takelbase](https://github.com/takelwerk/takelage-img-takelbase)* | [![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-img-takelbase/Build%20and%20deploy%20takelbase?label=deploy%20project)](https://github.com/takelwerk/takelage-img-takelbase/actions/workflows/build_deploy_takelbase_nightly.yml) |

## Installation

Install the pytest-takeltest pytest 
[plugin](https://pypi.org/project/takeltest/)
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

## Fixture testpass

You can access [gopass](https://www.gopass.pw/)
secrets by using the *testpass* fixture:

```python
def test_mytest(testpass):

    my_password = testpass('my_project/my_password')
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
using the ansible python api.

*multitestvars* creates a symbolic link to the roles directory of your 
ansible project in the ephemeral playbook environment which molecule sets up.
It then runs a playbook with ``gather_facts:true`` and a debug task 
to get the ansible variables and the ansible facts of the play and host.

*multitestvars* uses the ansible 
[VariableManager](https://github.com/ansible/ansible/blob/93ea9612057d47b28c9c42d439ef5679351b762b/lib/ansible/vars/manager.py#L74)
so the usual ansible variable 
[precedence rules](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable)
apply. Internally, the fixture uses the ansible
[debug module](https://docs.ansible.com/ansible/latest/modules/debug_module.html)
to resolve templates which have not been resolved by the
[setup module](https://docs.ansible.com/ansible/latest/modules/setup_module.html)
through the gather facts task.
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
[bitboard_provisioner scenario](test/system/anarchism/molecule/bitboard_provisioner)
and the
[bitboard_verifier scenario](test/system/anarchism/molecule/bitboard_verifier)
of the anarchism project. 
Omitting ``molecule converge`` and ``molecule idempotence`` has the
advantage that your pytests are automagically included.

Both scenarios achieve the same thing but they use different methods.
The bitboard server happens to be built with the same role
[takel-anarchism](test/system/anarchism/roles/takel-anarchism)
whose unit tests are applied in this scenarios to the
[bitboard server](https://github.com/takelwerk/takelage-bit)
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

## Ansible Python API

The pytest-takeltest plugin provides four main pytest fixtures
(and a couple of command line, environment variables and helper fixtures):

- *testpass* – exposes the ansible 
[passwordstore plugin](https://docs.ansible.com/ansible/latest/plugins/lookup/passwordstore.html)
- *multitestvars* – resolves and exposes ansible vars and facts 
    of all molecule hosts
- *testvars* – resolves and exposes ansible vars and facts 
    of one molecule host
- *moleculebook* – api to run playbooks against a molecule host
- *moleculeplay* – api to leverage the ansible python api

The *multitestvars*, *testvars* and *testpass* fixtures use the 
*moleculebook* fixture which in turn uses the *moleculeplay* fixture. 
*moleculeplay* makes low-level calls to the
[ansible python api](https://docs.ansible.com/ansible/latest/dev_guide/developing_api.html)
and uses the *moleculeenv* fixture to
handle the sysadmin tasks of setting the right symlinks.
*moleculeplay* and *moleculeenv* will probably not be very useful on their own
but *moleculebook* might be handy in those situations where you know you
shouldn't implement a hackaround. ;-)

Here is how you could run an ansible playbook programmatically from 
a test (or even better: from a 
[fixture](https://docs.pytest.org/en/latest/fixture.html)) using dependency injection.

```python
def test_takeltest_moleculebook(host, moleculebook):
    playbook = moleculebook.get()
    args = dict(path='/tmp/moleculebook_did_this', state='touch')
    task_touch = dict(action=dict(module='file', args=args))
    playbook['tasks'].append(task_touch)
    moleculebook.set(playbook)
    moleculebook.run()
    assert host.file('/tmp/moleculebook_did_this').exists
```

See 
[takel-gem](https://github.com/takelwerk/takelage-dev/blob/master/ansible/roles/takel-gem/molecule/default/system/test_takel-gem_system.py)
for a real-world example where moleculebook is used 
to avoid a molecule ``prepare.yml`` playbook
which otherwise needs to be copied 
to the project's molecule default scenario.
