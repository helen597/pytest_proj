import pytest

DICTIONARY = {"cat": "кошка", "doc": "собака", "chicken": "курица", "cow": "корова", "goat": "коза"}
@pytest.fixture
def dictionary_fixture():
    return DICTIONARY.copy()