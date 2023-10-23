import pytest

from utils import arrs


ARRAY = [1,2,3]
@pytest.fixture
def array_fixture():
    return ARRAY.copy()

def test_get(array_fixture):
    assert arrs.get(array_fixture, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(array_fixture):
    assert arrs.my_slice(array_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(array_fixture, 1) == [2, 3]
    assert arrs.my_slice([], 1, 3) == []
    assert arrs.my_slice(array_fixture) == array_fixture
    assert arrs.my_slice(array_fixture, 1, 5) == [2, 3]
