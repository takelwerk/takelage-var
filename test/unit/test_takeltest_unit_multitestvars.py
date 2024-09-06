import re
import takeltest
from takeltest.multitestvars import MultiTestVars


def test_takeltest_unit_multitestvars_cache_key(cache_key):
    assert re.match('multitestvars/+', cache_key)
