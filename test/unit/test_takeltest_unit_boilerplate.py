import takeltest
import testinfra


def test_takeltest_unit_boilerplate_hosts_no_molecule_inventory_file(
        monkeypatch):
    try:
        monkeypatch.delenv('MOLECULE_INVENTORY_FILE')
    except KeyError:
        pass
    hosts = takeltest.boilerplate.hosts()
    assert hosts == []


def test_takeltest_unit_boilerplate_hosts_molecule_inventory_file(
        monkeypatch):
    monkeypatch.setenv('MOLECULE_INVENTORY_FILE', 'localhost')
    monkeypatch.setattr(testinfra.utils.ansible_runner.AnsibleRunner,
                        'get_hosts',
                        lambda x, y: ['testhost'])
    hosts = takeltest.boilerplate.hosts()
    assert hosts == ['testhost']
