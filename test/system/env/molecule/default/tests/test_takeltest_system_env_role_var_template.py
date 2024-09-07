def test_takeltest_system_env_role_var_template_resolves(
        testvars):
    curl_my_var = testvars['curl_my_var']
    curl_my_ref = testvars['curl_my_ref']
    assert 'curl_my_value' == curl_my_var
    assert 'curl_my_value' == curl_my_ref
