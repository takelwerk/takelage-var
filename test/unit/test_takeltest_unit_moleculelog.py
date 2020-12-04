import takeltest
from takeltest.moleculelog import MoleculeLog


def test_takeltest_unit_moleculelog_is_not_none(moleculelog):
    assert moleculelog is not None


def test_takeltest_unit_moleculelog_debug():
    moleculelog = MoleculeLog()
    moleculelog.debug('test message')
    log = moleculelog.get_log()
    assert log == 'test message\n'


def test_takeltest_unit_moleculelog_print_debug_none(
        capsys,
        moleculelog,
        monkeypatch):
    monkeypatch.setattr(takeltest.moleculelog.MoleculeLog,
                        'get_log',
                        lambda x: '')
    expected_out = ''
    moleculelog.print_debug()
    captured = capsys.readouterr()
    assert captured.out == expected_out


def test_takeltest_unit_moleculelog_print_debug_os(
        capsys,
        moleculelog,
        monkeypatch):
    monkeypatch.setenv('TESTVARS_TESTENV', 'testvalue')
    monkeypatch.setattr(takeltest.moleculelog.MoleculeLog,
                        'get_log',
                        lambda x: '')
    expected_out = '\n\n' \
                   'TESTVARS ENVIRONMENT\n' \
                   "{'TESTVARS_TESTENV': 'testvalue'}\n"
    moleculelog.print_debug()
    captured = capsys.readouterr()
    assert captured.out == expected_out


def test_takeltest_unit_moleculelog_print_debug_log(
        capsys,
        moleculelog,
        monkeypatch):
    monkeypatch.setattr(takeltest.moleculelog.MoleculeLog,
                        'get_log',
                        lambda x: 'my_log_message\n')
    expected_out = '\n\nTESTVARS LOG' \
                   '\nmy_log_message\n\n'
    moleculelog.print_debug()
    captured = capsys.readouterr()
    assert captured.out == expected_out


def test_takeltest_unit_moleculelog_print_debug_os_and_log(
        capsys,
        moleculelog,
        monkeypatch):
    monkeypatch.setenv('TESTVARS_TESTENV', 'testvalue')
    monkeypatch.setattr(takeltest.moleculelog.MoleculeLog,
                        'get_log',
                        lambda x: 'my_log_message\n')
    expected_out = '\n\n' \
                   'TESTVARS ENVIRONMENT\n' \
                   "{'TESTVARS_TESTENV': 'testvalue'}\n" \
                   'TESTVARS LOG\n' \
                   'my_log_message\n\n'

    moleculelog.print_debug()
    captured = capsys.readouterr()
    assert captured.out == expected_out
