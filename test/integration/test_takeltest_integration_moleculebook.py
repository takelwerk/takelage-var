def test_takeltest_integration_moleculebook_run_task_get_vars(moleculebook):
    moleculebook.create()
    playbook = moleculebook.get()
    playbook = playbook | {'vars': {'myvar': 'myvalue', 'myvarref': '{{ myvar }}'}}
    playbook['gather_facts'] = 'False'
    moleculebook.set(playbook)
    vars = moleculebook.get_vars()
    assert vars['myvarref'] == 'myvalue'
