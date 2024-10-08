import json
import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_system_templates_resolve_template_string(
        testvars):
    assert testvars['project_my_var_1'] == 'my_string_1'


def test_takeltest_system_templates_resolve_template_string_reference(
        testvars):
    assert testvars['project_template1'] == 'my_string_1'


def test_takeltest_system_templates_resolve_template_string_twice(
        testvars):
    assert testvars['project_template2'] == 'my_string_1'


def test_takeltest_system_templates_resolve_template_string_transitive(
        testvars):
    assert testvars['project_template3'] == 'my_string_1'


def test_takeltest_system_templates_resolve_template_string_inline_front(
        testvars):
    assert testvars['project_template4'] == 'inline+my_string_1'


def test_takeltest_system_templates_resolve_template_string_inline_back(
        testvars):
    assert testvars['project_template5'] == 'my_string_1+inline'


def test_takeltest_system_templates_resolve_template_string_inline_both(
        testvars):
    assert testvars['project_template6'] == 'inline+my_string_1+inline'


def test_takeltest_system_templates_resolve_template_no_string(
        testvars):
    assert testvars['project_my_var_2'] == 99


def test_takeltest_system_templates_resolve_template_no_string_reference(
        testvars):
    assert testvars['project_template7'] == 99


def test_takeltest_system_templates_resolve_template_no_string_transitive(
        testvars):
    # FIXME: Why is this suddenly a string?
    assert testvars['project_template8'] == '99'


def test_takeltest_system_templates_resolve_template_no_string_inline_front(
        testvars):
    assert testvars['project_template9'] == 'inline+99'


def test_takeltest_system_templates_resolve_template_no_string_inline_back(
        testvars):
    assert testvars['project_template10'] == '99+inline'


def test_takeltest_system_templates_resolve_template_no_string_inline_both(
        testvars):
    assert testvars['project_template11'] == 'inline+99+inline'


def test_takeltest_system_templates_resolve_template_special_chars_1(
        testvars):
    assert testvars['project_special1'] == "äö(ü'!)§$;~é"


def test_takeltest_system_templates_resolve_template_special_chars_2(
        testvars):
    assert testvars['project_special2'] == 'ñô‰(„}»")¯]¿¬'


def test_takeltest_system_template_resolve_lookup(
        testvars):
    assert testvars['project_lookup_flattened'] == [1, 2, 3, 4, 5, 6]


def test_takeltest_system_templates_resolve_template_list(
        testvars):
    list1_json = '["first_list_item", "second_list_item"]'
    assert json.dumps(testvars['project_list1']) == list1_json


def test_takeltest_system_templates_resolve_template_nested_list(
        testvars):
    list2_json = '["first_list_item", "second_list_item"]'
    assert isinstance(testvars['project_list2'], list)
    assert json.dumps(testvars['project_list2']) == list2_json


def test_takeltest_system_templates_resolve_template_dict(
        testvars):
    dict1_json = '{"first_key": "first_value", "second_key": "second_value"}'
    assert json.dumps(testvars['project_dict1']) == dict1_json


def test_takeltest_system_templates_resolve_template_filter_zip(
        testvars):
    filter_zip_json = '[["first_list_item", "anarchism"], '
    filter_zip_json += '["second_list_item", "fortune-anarchism"]]'
    assert json.dumps(testvars['project_filter_zip']) == filter_zip_json


def test_takeltest_system_templates_resolve_template_filter_dict2items(
        testvars):
    filter_dict_json = '[{"key": "first_key", '
    filter_dict_json += '"value": "first_value"}, '
    filter_dict_json += '{"key": "second_key", '
    filter_dict_json += '"value": "second_value"}]'
    assert json.dumps(testvars['project_filter_dict2items']) == \
        filter_dict_json
