import pytest
from utils.dicts import get_val


@pytest.mark.parametrize('dictionary, key, default, expected', [
    ({}, "cat", "test", "test"),
    ("dictionary_fixture", "cat", "test", "кошка"),
    ("dictionary_fixture", "duck", "test", "test")
])


def test_dicts(dictionary, key, default, expected, request):
    if dictionary == "dictionary_fixture":
        assert get_val(request.getfixturevalue(dictionary), key, default) == expected
    else:
        assert get_val(dictionary, key, default) == expected
