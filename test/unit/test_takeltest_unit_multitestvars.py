import re


def test_takeltest_unit_multitestvars_cache_key(cache_key):
    assert re.match('multitestvars/+', cache_key)
