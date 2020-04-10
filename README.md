# takelage-var

*takelage-var* provides the [pytest](https://pytest.org/)
plugin [takeltest](https://pypi.org/project/takeltest/)
for the takelage devops workflow.
The takelage devops workflow helps devops engineers
build, test and deploy os images.

The pytest plugin 
[testinfra](https://testinfra.readthedocs.io/en/latest/)
allows to write unit tests in python to test
your servers configured by the management tool 
[ansible](https://www.ansible.com/).
testinfra is the default 
[verifier](https://molecule.readthedocs.io/en/stable/configuration.html#testinfra)
of the [molecule]( https://molecule.readthedocs.io/)
testing environment.

The pytest plugin takeltest provides helper functions
and fixtures to facilitate the use of molecule and testinfra.
It provides access to variables and secrets and helps to not only 
to unit test your ansible roles but to
integration and system test your whole ansible project.

testinfra wraps 
[cli](https://philpep.org/blog/infrastructure-testing-with-testinfra) 
calls to the ansible executable.
takeltest uses the ansible python
[api](https://docs.ansible.com/ansible/latest/dev_guide/developing_api.html)
to run ansible playbooks.

## Framework

The takelage devops framework consists of these projects:

| App | Description |
| --- | ----------- |
| *[takelage-doc](https://github.com/geospin-takelage/takelage-doc)* | takelage documentation |
| *[takelage-dev](https://github.com/geospin-takelage/takelage-dev)* | takelage development environment |
| *[takelage-var](https://github.com/geospin-takelage/takelage-var)* | takelage test plugin |
| *[takelage-cli](https://github.com/geospin-takelage/takelage-cli)* | takelage command line interface |
| *[takelage-bit](https://github.com/geospin-takelage/takelage-bit)* | takelage bit server | 

## Installation

Install the takeltest pytest 
[plugin](https://pypi.org/project/takeltest/)
using [pip](https://packaging.python.org/tutorials/installing-packages/):

```bash
pip install takeltest
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
[ruby](test/system/ruby)
system test directories for examples
of molecule projects using ansible, testinfra and takeletst.

## Boilerplate

As a boilerplate for testinfra tests it is enough to do:

```python
import takeltest

testinfra_hosts = takeltest.hosts()
``` 

## Fixture testpass

You can access [gopass](https://www.gopass.pw/)
secrets by using the *testpass* fixture:

```python
def test_mytest(testpass):

    my_password = testpass('my_project/my_password')
```

## Fixture testvars

Arguably the most useful feature of the takeltest plugin
is the *testvars* fixture.
The *testvars* fixture resolves and exposes 
ansible variables as a python dict:

```python
def test_mytest(testvars):

    my_variable = testvars['my_variable']
```

*testvars* runs a playbook against the molecule host using the ansible python api.

*testvars* creates a symbolic link to the roles directory of your ansible project
in the ephemeral playbook environment which molecule sets up.
It then runs a playbook with ``gather_facts:true`` and a debug task 
to get the ansible variables and the ansible facts of the play and host.

*testvars* uses the ansible 
[VariableManager](https://github.com/ansible/ansible/blob/93ea9612057d47b28c9c42d439ef5679351b762b/lib/ansible/vars/manager.py#L74)
so the usual ansible variable 
[precedence rules](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable)
apply. Internally, the fixture uses the ansible
[debug module](https://docs.ansible.com/ansible/latest/modules/debug_module.html)
to resolve templates which have not been resolved by the
[setup module](https://docs.ansible.com/ansible/latest/modules/setup_module.html)
through the gather facts task.
Thus, it can resolve any kind of template that the debug module can resolve including
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

Which roles are included is determined in this order:

- List of roles separated by colon specified in the
  ``TESTVARS_ROLES_WHITELIST`` environment variable
- List of roles specified in playbook speciied in ``molecule.yml``
- List of roles specified in default playbook ``playbook.yml``
- All roles in ``roles`` directory in project directory

Roles blacklisted in ``TESTVARS_ROLES_BLACKLIST`` won't be included.

### options

testvars is a session scope fixture so its configuration is done in
``molecule.yml`` by using pytest command line options.
You can add a couple of options in the options dictionary
of the verifier section:

```yaml
verifier:
  name: testinfra
  options:
    testvars-no-gather-facts: true
```

By default, testvars runs a playbook to gather ansible variables and facts.
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

Hopefully the testvars fixture allows fast test-driven development.
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

You should use the takeltest boilerplate code to be able to run pytest directly.
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

The takeltest plugin provides four main pytest fixtures
(and a couple of command line, environment variables and helper fixtures):

- testpass – exposes the ansible 
[passwordstore plugin](https://docs.ansible.com/ansible/latest/plugins/lookup/passwordstore.html)
- testvars – resolves and exposes ansible vars and facts
- moleculebook – api to run playbooks against a molecule host
- moleculeplay – api to leverage the ansible python api

The testvars and testpass fixtures use the moleculebook fixture which in turn
uses the moleculeplay fixture. moleculeplay makes low-level calls to the
[ansible python api](https://docs.ansible.com/ansible/latest/dev_guide/developing_api.html)
and uses the moleculeenv fixture to
handle the sysadmin tasks of setting the right symlinks.
moleculeplay and moleculeenv will probably not be very useful on their own
but moleculebook might be handy in those situations where you know you
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
[takel-gem](https://github.com/geospin-takelage/takelage-dev/blob/master/ansible/roles/takel-gem/molecule/default/system/test_takel-gem_system.py)
for a real-world example where moleculebook is used 
to avoid a molecule prepare.yml playbook
which otherwise needs to be copied 
to the project's molecule default scenario.
